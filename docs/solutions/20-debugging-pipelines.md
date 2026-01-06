# Solution: Debugging Pipelines

## Solution Overview

This solution covers debugging Collector pipeline issues.

## Step-by-Step Solution

### Task 1: Identify Pipeline Issues

**Common Symptoms**:
- No data in Jaeger/Prometheus
- Collector errors in logs
- Configuration syntax errors
- Component failures

**Check**: `docker logs otel-collector`

### Task 2: Inspect Collector Logs

**View Logs**:
```bash
docker logs otel-collector
docker logs otel-collector --follow
docker logs otel-collector --tail 100
```

**Look For**:
- Configuration errors
- Export failures
- Processing errors
- Component initialization issues

### Task 3: Verify Pipeline Configuration

**Validate Configuration**:
```bash
docker exec otel-collector /otelcol --config=/etc/otel-config.yaml --dry-run
```

**Common Issues**:
- YAML syntax errors
- Component name mismatches
- Missing component references
- Invalid configuration values

### Task 4: Debug Data Flow

**Check Each Stage**:
1. **Receivers**: Verify data is received
   - Check receiver logs
   - Verify endpoints are accessible

2. **Processors**: Verify processing
   - Check processor logs
   - Verify processor configuration

3. **Exporters**: Verify export
   - Check exporter logs
   - Verify backend connectivity
   - Test backend endpoints

**Debugging Steps**:
```bash
# Check Collector health
curl http://localhost:13133

# Check if receiving data
docker logs otel-collector | grep "Received"

# Check export status
docker logs otel-collector | grep "Export"
```

## Key Takeaways

- Use Collector logs for debugging
- Validate configuration syntax
- Check each pipeline stage
- Verify backend connectivity
