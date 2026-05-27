# Backend

> Library management REST API with admin UI

## Overview

A fully containerized backend system for managing a library — handling books, loans, fines, and reservations. Includes an admin UI for library staff and is built for deployment with Docker.

## Features

- Book catalog management (add, update, remove)
- Loan tracking with due dates
- Fine calculation for overdue items
- Reservation system
- Admin UI for library staff
- Dockerized for easy deployment

## Tech Stack

| Area | Technology |
|------|-----------|
| Language | Python |
| Framework | FastAPI |
| ORM | SQLAlchemy |
| Containerization | Docker |

## Highlights

- FastAPI provides automatic OpenAPI docs out of the box
- SQLAlchemy ORM abstracts database operations cleanly across all models
- Docker setup makes it portable — spin up the full stack with one command

## Screenshots

<p align="center">
  <img src="assets/backend/swagger-docs.png" width="160"/>
</p>

> _Backend has no app UI — a screenshot of the auto-generated FastAPI `/docs` (Swagger) page or the admin UI works best. Add it to `projects/assets/backend/` and update the filename above._

## Links

- [GitHub](https://github.com/cobra-PICH/Backend)
