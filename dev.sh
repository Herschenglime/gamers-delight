#!/usr/bin/env sh

cd api

uvicorn main:app --reload &

cd ../frontend

npm run dev -- --open
