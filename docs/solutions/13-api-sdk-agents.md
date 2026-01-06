# Solution: Agents

## Solution Overview

This solution covers understanding OpenTelemetry agents and the Collector's agent role.

## Step-by-Step Solution

### Task 2: Identify Agent-like Components

**OpenTelemetry Collector as Agent**:

- Receives telemetry from services (agent role)
- Processes telemetry data
- Exports to backends
- Acts as intermediary

**Current Setup** (`docker-compose.yaml`):

```yaml
otel-collector:
  image: otel/opentelemetry-collector:latest
  # Receives from services, exports to Jaeger/Prometheus
```

### Task 3: Understand Auto-Instrumentation

**Express Instrumentation** (automatic):

- No code changes needed
- Automatically creates spans
- Adds HTTP attributes
- Similar to agent behavior

**Flask Instrumentation** (automatic):

- No code changes needed
- Automatically creates spans
- Adds HTTP attributes
- Similar to agent behavior

### Task 4: Compare Agent vs SDK

**Agent Approach**:

- No code changes
- Easier setup
- Language-specific agents
- Less control

**SDK Approach** (current system):

- Programmatic control
- Custom instrumentation
- More flexibility
- Code changes required

## Key Takeaways

- Collector acts as agent
- Auto-instrumentation is agent-like
- Agents: easier, less control
- SDK: more control, more setup
