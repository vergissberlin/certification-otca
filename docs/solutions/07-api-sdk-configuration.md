# Solution: Configuration

## Solution Overview

This solution covers configuring OpenTelemetry using environment variables and programmatic configuration.

## Step-by-Step Solution

### Task 2: Configure via Environment Variables

Add to `docker-compose.yaml` for Node service:

```yaml
service-node:
  environment:
    OTEL_EXPORTER_OTLP_ENDPOINT: "http://otel-collector:4317"
    OTEL_TRACES_EXPORTER: otlp
    OTEL_METRICS_EXPORTER: otlp
    OTEL_SERVICE_NAME: "service-node"
    OTEL_TRACES_SAMPLER: "always_on"
    OTEL_LOG_LEVEL: "info"
```

**Verification**: Restart service and check configuration is applied.

### Task 3: Configure Programmatically

Modify `service-python/app.py` to add more programmatic configuration:

```python
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.sdk.resources import Resource

resource = Resource.create({
    "service.name": "service-python",
    "service.version": "1.0.0"
})

tracer_provider = TracerProvider(resource=resource)
trace.set_tracer_provider(tracer_provider)

# Configure span processor with options
span_processor = BatchSpanProcessor(
    OTLPSpanExporter(),
    max_queue_size=2048,
    max_export_batch_size=512,
    export_timeout_millis=30000,
    schedule_delay_millis=5000
)
tracer_provider.add_span_processor(span_processor)
```

### Task 4: Configuration Precedence

**Precedence Order**:
1. Programmatic configuration (highest)
2. Environment variables
3. Default values (lowest)

**Best Practices**:
- Use environment variables for deployment flexibility
- Use programmatic config for application-specific settings
- Document configuration sources

## Key Takeaways

- Environment variables: Deployment flexibility
- Programmatic: Application control
- Programmatic overrides environment
- Use appropriate method for use case
