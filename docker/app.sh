#!/bin/bash

alembic upgrade head

uvicorn app:app --host 0.0.0.0 --reload