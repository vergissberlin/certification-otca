# Solution: Collector Scaling

## Solution Overview

This solution covers scaling the OpenTelemetry Collector.

## Step-by-Step Solution

### Task 2: Configure Horizontal Scaling

Modify `docker-compose.yaml` to add multiple Collector instances:

```yaml
otel-collector-1:
  image: otel/opentelemetry-collector:latest
  volumes:
    - ./otel-config.yaml:/etc/otel-config.yaml
  command: ["--config=/etc/otel-config.yaml"]
  ports:
    - "4317:4317"

otel-collector-2:
  image: otel/opentelemetry-collector:latest
  volumes:
    - ./otel-config.yaml:/etc/otel-config.yaml
  command: ["--config=/etc/otel-config.yaml"]
  ports:
    - "4318:4317"
```

**Note**: In production, use load balancer to distribute traffic.

### Task 3: Configure Vertical Scaling

Modify `docker-compose.yaml`:

```yaml
otel-collector:
  deploy:
    resources:
      limits:
        memory: 2G
        cpus: '2.0'
      reservations:
        memory: 1G
        cpus: '1.0'
```

**Monitor**: Use `docker stats otel-collector` to monitor resource usage.

## Key Takeaways

- Horizontal: More instances
- Vertical: More resources per instance
- Monitor to determine scaling needs
- Balance cost and performance
