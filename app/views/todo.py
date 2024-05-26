from flask import abort
from flask.views import MethodView
from flask_smorest import Blueprint
from app.schemas import CreateTask, UpdateTask, Task, ListTasks, ListTasksParameters, SortByEnum, SortDirectionEnum
from app.models import tasks
from utils import uuid_generator, current_time

todo = Blueprint("todo", __name__, url_prefix="/todo", description="TODO API")

@todo.route("/tasks")
class TodoCollection(MethodView):

    @todo.arguments(ListTasksParameters, location="query")
    @todo.response(status_code=200, schema=ListTasks)
    def get(self, parameters):
        return { 
            "tasks": sorted(
                tasks, 
                key=lambda task: task[parameters["order_by"].value],
                reverse=parameters["order"] == SortDirectionEnum.desc,
            )
        }

@todo.route("/task")
class TodoCollection(MethodView):

    @todo.arguments(CreateTask)
    @todo.response(status_code=201, schema=Task)
    def post(self, task):
        task["id"] = uuid_generator.get_uuid()
        task["created"] = current_time.get_now()
        task["completed"] = False
        tasks.append(task)
        return task

@todo.route("/tasks/<string:task_id>")
class TodoTask(MethodView):

    @todo.response(status_code=200, schema=Task)
    def get(self, task_id):
        for task in tasks:
            if task["id"] == task_id:
                return task
        abort(404, f"Task with ID {task_id} not found.")

    @todo.arguments(UpdateTask)
    @todo.response(status_code=200, schema=Task)
    def put(self, payload, task_id):
        for task in tasks:
            if task["id"] == task_id:
                task["completed"] = payload["completed"]
                task["task"] = payload["task"]
                return task
        abort(404, f"Task with ID {task_id} not found.")

    @todo.response(status_code=204)
    def delete(self, task_id):
        for index, task in enumerate(tasks):
            if task["id"] == task_id:
                tasks.pop(index)
                return
        abort(404, f"Task with ID {task_id} not found.")
