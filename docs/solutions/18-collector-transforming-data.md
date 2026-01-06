# Solution: Transforming Data

## Solution Overview

This solution covers transforming telemetry data in the Collector.

## Step-by-Step Solution

### Task 2: Add Attributes Processor

Modify `otel-config.yaml`:

```yaml
processors:
  batch:
  attributes:
    actions:
      - key: environment
        value: development
        action: insert
      - key: region
        value: us-east-1
        action: insert

service:
  pipelines:
    traces:
      receivers: [otlp]
      processors: [batch, attributes]
      exporters: [jaeger]
```

**Verification**: Check Jaeger → Spans should have `environment` and `region` attributes.

### Task 3: Add Resource Processor

Modify `otel-config.yaml`:

```yaml
processors:
  batch:
  resource:
    attributes:
      - key: deployment.environment
        value: production
        action: upsert

service:
  pipelines:
    traces:
      receivers: [otlp]
      processors: [batch, resource]
      exporters: [jaeger]
```

### Task 4: Use Transform Processor

Modify `otel-config.yaml`:

```yaml
processors:
  batch:
  transform:
    trace_statements:
      - context: span
        statements:
          - set(attributes["processed"], true) where name == "hello-span"

service:
  pipelines:
    traces:
      receivers: [otlp]
      processors: [batch, transform]
      exporters: [jaeger]
```

**Note**: Transform processor uses OTTL (OpenTelemetry Transformation Language).

## Key Takeaways

- Attributes processor: Modify span attributes
- Resource processor: Modify resource attributes
- Transform processor: Complex transformations
- Processors transform data before export
