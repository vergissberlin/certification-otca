# Solution: Collector Pipelines

## Solution Overview

This solution covers understanding and configuring Collector pipelines.

## Step-by-Step Solution

### Task 3: Modify Pipeline Components

Add a new processor to `otel-config.yaml`:

```yaml
processors:
  batch:
  attributes:
    actions:
      - key: environment
        value: development
        action: insert

service:
  pipelines:
    traces:
      receivers: [otlp]
      processors: [batch, attributes]
      exporters: [jaeger]
```

**Note**: Processor order matters. `attributes` before `batch` processes before batching.

### Task 4: Create Multiple Pipelines

Create separate pipelines for different backends:

```yaml
exporters:
  jaeger:
    endpoint: "http://jaeger:14268/api/traces"
  otlp/backend2:
    endpoint: "http://backend2:4317"

service:
  pipelines:
    traces:
      receivers: [otlp]
      processors: [batch]
      exporters: [jaeger, otlp/backend2]
```

## Key Takeaways

- Pipelines: receivers → processors → exporters
- Processor order matters
- Multiple pipelines per signal possible
- Separate pipelines for different backends
