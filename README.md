# Git and GitHub - Vaibhav Naik

Flask + MongoDB project used to demonstrate the Git and GitHub workflow
(branches, merges, conflict resolution, reset and rebase).

## Project layout

```
app.py                  Flask application
data.json               JSON served by the /api route
requirements.txt        Python dependencies
templates/form.html     Student registration form
templates/success.html  Submission success page
templates/todo.html     To-Do form page
```

## Setup

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

Create a `.env` file in the project root (it is git-ignored):

```
MONGO_URI=mongodb://localhost:27017
```

## Run

```bash
python app.py
```

## Routes

| Route              | Method    | Description                                  |
| ------------------ | --------- | -------------------------------------------- |
| `/`                | GET/POST  | Student registration form, stores in MongoDB  |
| `/success`         | GET       | Success page                                  |
| `/api`             | GET       | Returns the contents of `data.json`           |
| `/todo`            | GET       | To-Do form page                               |
| `/submittodoitem`  | POST      | Stores a To-Do item in MongoDB                |

## Branches

| Branch           | Purpose                                              |
| ---------------- | ---------------------------------------------------- |
| `main`           | Base branch, holds the merged result                 |
| `VaibhavNaik`    | Task 1 - initial Flask project files                 |
| `VaibhavNaik_new`| Task 2 - updated `data.json` for the `/api` route    |
| `master_1`       | Task 3 / Task 4 - To-Do frontend form                |
| `master_2`       | Task 3 - `/submittodoitem` backend route             |