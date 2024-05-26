

from utils import current_time, uuid_generator


tasks = [
    {
        "id": uuid_generator.get_uuid(),
        "created": current_time.get_now(),
        "completed": False,
        "task": "Create Flask API",
    }
]
