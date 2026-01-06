# Solution: Collector Deployment

## Solution Overview

This solution covers deploying the OpenTelemetry Collector.

## Step-by-Step Solution

### Task 2: Modify Deployment Configuration

Modify `docker-compose.yaml`:

```yaml
otel-collector:
  image: otel/opentelemetry-collector:latest
  container_name: otel-collector
  volumes:
    - ./otel-config.yaml:/etc/otel-config.yaml
  command: ["--config=/etc/otel-config.yaml"]
  ports:
    - "4317:4317"
    - "55681:55681"
  environment:
    - OTEL_COLLECTOR_LOG_LEVEL=info
  deploy:
    resources:
      limits:
        memory: 512M
        cpus: '0.5'
      reservations:
        memory: 256M
        cpus: '0.25'
```

### Task 3: Deployment Patterns

**Current Pattern**: Gateway (centralized)
- Single Collector for all services
- Centralized processing
- Easier management

**Alternative Patterns**:
- **Sidecar**: One Collector per service
- **Agent**: One Collector per host/node

### Task 4: Configure Health Checks

Add to `docker-compose.yaml`:

```yaml
otel-collector:
  healthcheck:
    test: ["CMD", "wget", "--spider", "-q", "http://localhost:13133"]
    interval: 30s
    timeout: 10s
    retries: 3
    start_period: 40s
```

**Verification**: `docker ps` shows health status.

## Key Takeaways

- Docker deployment is common
- Gateway pattern: centralized
- Resource limits prevent overload
- Health checks monitor status
