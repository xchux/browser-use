# Codebase Structure

> The code structure inspired by https://github.com/Netflix/dispatch.

Very good structure on how to make a scalable codebase is also in [this repo](https://github.com/zhanymkanov/fastapi-best-practices).

Just a brief document about how we should structure our backend codebase.

## Code Structure

```markdown
src/
/<service name>/
models.py
services.py
prompts.py
views.py
utils.py
routers.py

    	/_<subservice name>/
```

### Service.py

Always a single file, except if it becomes too long - more than ~500 lines, split it into \_subservices

### Views.py

Always split the views into two parts

```python
# All
...

# Requests
...

# Responses
...
```

If too long → split into multiple files

### Prompts.py

Single file; if too long → split into multiple files (one prompt per file or so)

### Routers.py

Never split into more than one file


### Architecture diagram

```mermaid
graph TD
    subgraph Agent Layer
        AgentService["Agent (service.py)"]
        Memory["Memory (memory/service.py)"]
        MessageManager["MessageManager (message_manager/service.py)"]
        Prompts["Prompts (prompts.py)"]
        Views["Views (views.py)"]
    end

    subgraph Browser Layer
        Browser["Browser (browser/browser.py)"]
        BrowserContext["BrowserContext (browser/context.py)"]
        DOMService["DOM Service (dom/service.py)"]
        DOMHistory["DOM History Processor (dom/history_tree_processor/service.py)"]
    end

    subgraph Controller Layer
        Controller["Controller (controller/service.py)"]
        Registry["Registry (controller/registry/service.py)"]
        Actions["Actions (controller/registry/views.py)"]
    end

    subgraph Telemetry Layer
        Telemetry["Telemetry (telemetry/service.py)"]
    end

    AgentService --> Memory
    AgentService --> MessageManager
    AgentService --> Prompts
    AgentService --> Views
    AgentService --> Controller
    AgentService --> Browser
    AgentService --> Telemetry

    MessageManager --> Prompts
    MessageManager --> Views

    Controller --> Registry
    Registry --> Actions

    Browser --> BrowserContext
    Browser --> DOMService
    DOMService --> DOMHistory
```


