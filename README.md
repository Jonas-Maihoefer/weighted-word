last prompt: https://aistudio.google.com/u/1/prompts/1SnYaWU0ZlnOT3yD1JUo9_wTiC0AqX95J


# weighted-word
This tool analyzes the thematic distribution of Bible passages and compares it with sermon or verse selections. By mapping texts to established topical bibles, it reveals over- and underemphasized themes relative to the biblical canon.

## Project Description

"The bible talks about money way more than we do today." This tool tries to empirically quantify such statements.
It is intended for churches or pastors to perform topical analysis for sermons or quoted bible verses.
With it, shortcomings or overused topics in comparision to the emphases of the bilical canon can be brought to light.

## Underlying Mechanism

To determine the topic of individual bible verses and therefore the topic distribution of the biblical corpus we use 
`Nave's Topical Bible`, `Torrey's Topical Textbook` and biblehub.com's `Topical Bible Verses`.
Combined they have XXXXX topics and XXXXXX entries

Quoting the whole bible would result in perfect topic distribution, so inputting a subset of all bible verses into the tool 
results in a suboptimal topic distribution.
The input verses are first converted into their topics and counts given the meantioned topical encyclopedias. 
This step can be skipped if raw topics and their duration in church sermons are inputted.
The now obtained topic distribution can then be compared to the topic distribution of the bible to find outliars.


## How to dev

### Running the Backend
#### Development (hot reload)

Mac/Linux/WSL
```
uvicorn app.main:app --reload
```

Windows
```
.\dev.bat
```
(or double click on dev.bat)

#### Production
```
gunicorn -k uvicorn.workers.UvicornWorker app.main:app
```



### Folder structure

#### Project Root: `backend/`

This is the **root of your Python backend project**. It contains:

* `app/` – the main application code
* `tests/` – automated tests
* `pyproject.toml` – Python project metadata and dependencies
* `README.md` – documentation

The root should remain clean; no business logic should live here.


#### `app/` – Application Source Code

The `app/` folder contains **all the code for your FastAPI application**. It is organized according to **layered architecture**:

##### `main.py`

* **Purpose:** The entry point for the application.
* **Contents:** Creates the FastAPI app instance, includes routers, sets metadata like title and version.
* **Reason:** Keeps the app initialization separate from logic. Essential for hot reload, production deployment, and testing.

##### `core/` – Application Core Configuration

Contains **cross-cutting concerns** used across the app. Examples:

* `config.py`: Reads environment variables, centralizes settings like API URLs, environment, logging levels.
* `logging.py`: Configures logging for development and production.
* `lifespan.py`: Optional startup/shutdown events for database connections, cache warming, or scheduled tasks.

**Purpose:** Avoids magic constants scattered in code; provides a single source of truth for app configuration and lifecycle management.

##### `api/` – HTTP API Layer

Handles **all external HTTP exposure**. This layer should **not contain business logic**, only routing, validation, and request/response modeling.

* `router.py` – Root router that includes all versioned routers (e.g., v1, v2).
* `v1/` – Versioned API to support breaking changes in the future.

  * `router.py` – Aggregates endpoints in this version.
  * `endpoints/` – Individual HTTP endpoints grouped by resource:

    * `health.py` – Health check endpoint (`/health`)
    * `topics.py` – Endpoints related to Bible topic distributions (`/topics`)
    * `analysis.py` – Endpoints for comparing sermon inputs with Bible topics (`/analysis`)

**Purpose:**

* Provides **API versioning** and modularity.
* Makes the OpenAPI schema predictable.
* Supports hot reload and automatic TypeScript client generation.

##### `models/` – Pydantic Schemas

Contains **all API contracts** (request/response models) as **Pydantic classes**:

* `topic.py` – Defines topic distributions.
* `analysis.py` – Defines analysis input/output structures.

**Purpose:**

* Ensures **type-safe API contracts**.
* Provides validation, documentation, and OpenAPI integration.
* Guarantees that generated TypeScript clients are correct.


##### `services/` – Business Logic Layer

Contains **core computation and domain logic**, separated from HTTP and data access:

* `topic_service.py` – Logic to compute Bible topic distributions.
* `analysis_service.py` – Logic to compare input verses with canonical distributions.

**Purpose:**

* Centralizes all non-HTTP logic.
* Makes it testable independently of API calls.
* Keeps the codebase clean and maintainable.

##### `repositories/` – Data Access Layer

Handles **loading, saving, or querying data**. Examples:

* `topic_repository.py` – Loads Bible topic JSON or DB tables.
* `corpus_repository.py` – Reads sermons or external inputs.

**Purpose:**

* Abstracts data source (JSON, DB, S3, etc.).
* Makes it easy to swap storage without touching services or API.
* Separates I/O from computation.


##### `data/` – Static / Precomputed Data

Contains **raw or preprocessed data** files used by repositories:

* `bible_topics.json` – Example: precomputed topic distributions from Bible references.

**Purpose:**

* Provides quick access to reference datasets.
* Keeps data versioned alongside the application for reproducibility.


##### `__init__.py`

* Marks the `app` folder as a Python package.
* Optional: Can be used for app-wide imports or initialization hooks.


#### `tests/` – Automated Tests

Contains **unit and integration tests**, usually mirroring app structure:

```
tests/
  api/        ← Tests for endpoints (HTTP responses, validation)
  services/   ← Tests for business logic (topic analysis, computations)
```

**Purpose:**

* Ensures correctness and prevents regressions.
* Supports test-driven development.
* Allows CI/CD pipelines to validate API and service behavior.


#### Root Config Files

* **`pyproject.toml`** – Dependency management, build config.
* **`.env`** (optional) – Environment-specific variables (API keys, database URLs).
* **`README.md`** – Project description, setup instructions, and usage.

**Purpose:**

* Provides a clean starting point for deployment and collaboration.


##### ✅ Key Principles of This Structure

1. **Separation of Concerns**: API -> Services -> Repository -> Data are separate layers. Direction of dependencies is strictly one-way: Lower layers must never import from higher layers.
2. **Hot Reload Friendly**: `main.py` + `uvicorn --reload` works immediately.
3. **Production Ready**: Can plug in Gunicorn + Uvicorn, logging, and versioned APIs.
4. **OpenAPI/TypeScript Friendly**: Pydantic models → OpenAPI → TypeScript client generation.
5. **Testable**: Each layer is testable in isolation.
6. **Extensible**: Adding new endpoints, data sources, or versions is straightforward.

