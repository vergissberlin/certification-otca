# Solution: Semantic Conventions

## Solution Overview

This solution covers adding and using OpenTelemetry semantic conventions to improve observability data quality.

## Step-by-Step Solution

### Task 2: Add Resource Attributes

Modify `service-python/app.py`:

```python
from opentelemetry.sdk.resources import Resource

trace.set_tracer_provider(TracerProvider(
    resource=Resource.create({
        "service.name": "service-python",
        "service.version": "1.0.0",
        "service.namespace": "otca-training",
        "deployment.environment": "development"
    })
))
```

**Verification**: Check Jaeger UI → Select a trace → See resource attributes in trace details.

### Task 3: Add Custom Span Attributes

Modify the span in `service-python/app.py`:

```python
@app.route("/hello")
def hello():
    with tracer.start_as_current_span("hello-span") as span:
        span.set_attribute("user.id", "user123")
        span.set_attribute("request.method", "GET")
        span.set_attribute("response.status", 200)
        span.add_event("Processing request")
        counter.add(1)
        return "Hello from Python Service!"
```

**Verification**: Check Jaeger UI → Span details → See custom attributes and events.

### Task 4: HTTP Semantic Conventions

Automatic instrumentation adds:

- `http.method`: HTTP method (GET, POST, etc.)
- `http.route`: Route pattern
- `http.status_code`: HTTP status code
- `http.url`: Request URL

**Verification**: Check Jaeger UI → Span attributes → See HTTP semantic conventions automatically added.

## Key Takeaways

- Use semantic conventions when available (standardized)
- Add custom attributes for domain-specific data
- Resource attributes identify the service
- Span attributes provide request context
