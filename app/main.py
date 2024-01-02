from __future__ import annotations

import time
from typing import List, Optional, Union, Any

from fastapi import FastAPI, HTTPException

from .models import Dog, DogType, HTTPValidationError, Timestamp

app = FastAPI(
    title='FastAPI',
    version='0.1.0',
)

dogs_list = []
previous_id = 0


@app.get('/', response_model=Any)
def root__get() -> Any:
    return "Welcome!"


@app.get(
    '/dog', response_model=List[Dog], responses={'422': {'model': HTTPValidationError}}
)
def get_dogs_dog_get(kind: Optional[DogType] = None, ) -> Union[List[Dog], HTTPValidationError]:
    if kind:
        filtered_dogs = [dog for dog in dogs_list if dog.kind == kind]
        return filtered_dogs
    else:
        return dogs_list


@app.post('/dog', response_model=Dog, responses={'422': {'model': HTTPValidationError}})
def create_dog_dog_post(body: Dog) -> Union[Dog, HTTPValidationError]:
    dogs_list.append(body)
    return body


@app.get('/dog/{pk}', response_model=Dog, responses={'422': {'model': HTTPValidationError}})
def get_dog_by_pk_dog__pk__get(pk: int) -> Union[Dog, HTTPValidationError]:
    for dog in dogs_list:
        if dog.pk == pk:
            return dog
    raise HTTPException(status_code=404, detail="Dog not found")


@app.patch(
    '/dog/{pk}', response_model=Dog, responses={'422': {'model': HTTPValidationError}}
)
def update_dog_dog__pk__patch(pk: int, body: Dog = ...) -> Union[Dog, HTTPValidationError]:
    for dog in dogs_list:
        if dog.pk == pk:
            dog.name = body.name
            dog.kind = body.kind
            return dog
    raise HTTPException(status_code=404, detail="Dog not found")


@app.post('/post', response_model=Timestamp)
def get_post_post_post() -> Timestamp:
    global previous_id
    current_timestamp = int(time.time())
    previous_id += 1
    return Timestamp(id=previous_id, timestamp=current_timestamp)
