# Solution: Collector Configuration

## Solution Overview

This solution covers configuring the OpenTelemetry Collector.

## Step-by-Step Solution

### Task 2: Modify Receiver Configuration

Modify `otel-config.yaml`:

```yaml
receivers:
  otlp:
    protocols:
      grpc:
        endpoint: 0.0.0.0:4317
      http:
        endpoint: 0.0.0.0:55681
```

### Task 3: Modify Processor Configuration

Modify `otel-config.yaml`:

```yaml
processors:
  batch:
    timeout: 10s
    send_batch_size: 1024
    send_batch_max_size: 2048
```

### Task 4: Modify Exporter Configuration

Modify `otel-config.yaml`:

```yaml
exporters:
  jaeger:
    endpoint: "http://jaeger:14268/api/traces"
    tls:
      insecure: true
  prometheus:
    endpoint: "0.0.0.0:8888"
    const_labels:
      environment: "development"
```

### Task 5: Modify Pipeline Configuration

Modify `otel-config.yaml`:

```yaml
service:
  pipelines:
    traces:
      receivers: [otlp]
      processors: [batch]
      exporters: [jaeger]
    metrics:
      receivers: [otlp]
      processors: [batch]
      exporters: [prometheus]
```

**Verification**: Restart Collector and verify data flows.

## Key Takeaways

- Configuration is YAML format
- Sections: receivers, processors, exporters, service
- Pipelines connect components
- Validate configuration before deploying
