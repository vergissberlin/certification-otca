# Agents

**Exam Weight**: The OpenTelemetry API and SDK (46%)

## Learning Objectives

- Understand OpenTelemetry agents
- Learn about auto-instrumentation agents
- Understand agent vs SDK approach
- Learn agent configuration
- Understand when to use agents

## Prerequisites

- System is running
- Understanding of instrumentation
- Basic knowledge of agents

## Exercise Tasks

### Task 1: Understand Agent Concept

**Description**: Learn about OpenTelemetry agents and their role.

**Expected Outcome**:

- Understand what agents are
- Learn agent vs SDK approach
- Understand agent benefits
- Know agent use cases

**Hints**:

- Agents provide auto-instrumentation
- No code changes required
- Language-specific agents
- Alternative to SDK approach

**Reference Files**:

- OpenTelemetry agents documentation
- Current system uses SDK approach

### Task 2: Identify Agent-like Components

**Description**: Identify components in the system that act like agents.

**Expected Outcome**:

- Identify OpenTelemetry Collector as agent
- Understand Collector's agent role
- Understand agent responsibilities
- Document agent functionality

**Hints**:

- Collector acts as agent
- Receives telemetry from services
- Processes and exports data
- Agent-like functionality

**Reference Files**:

- `otel-config.yaml`
- `docker-compose.yaml` (Collector service)
- OpenTelemetry Collector documentation

### Task 3: Understand Auto-Instrumentation

**Description**: Understand how auto-instrumentation works (agent-like).

**Expected Outcome**:

- Understand automatic instrumentation
- Learn how it works without code changes
- Understand instrumentation libraries
- Know auto-instrumentation benefits

**Hints**:

- Express and Flask instrumentation
- Automatic span creation
- No manual code needed
- Similar to agent behavior

**Reference Files**:

- `service-node/app.js` (Express instrumentation)
- `service-python/app.py` (Flask instrumentation)
- Instrumentation libraries

### Task 4: Compare Agent vs SDK

**Description**: Compare agent approach with SDK approach.

**Expected Outcome**:

- Understand agent advantages
- Understand SDK advantages
- Know when to use each
- Document comparison

**Hints**:

- Agents: no code changes, easier setup
- SDK: more control, programmatic
- Current system uses SDK
- Both approaches valid

**Reference Files**:

- Current system (SDK approach)
- OpenTelemetry agents documentation

## Verification Steps

1. **Agent Concept Verification**:
   - Understand agent role
   - Know agent benefits
   - Understand agent use cases

2. **Agent-like Components Verification**:
   - Identify agent-like components
   - Understand Collector's role
   - Know agent responsibilities

3. **Auto-Instrumentation Verification**:
   - Understand auto-instrumentation
   - Know how it works
   - Understand benefits

4. **Comparison Verification**:
   - Understand agent vs SDK
   - Know when to use each
   - Make informed choice

## Solution

See [Solution: Agents](../solutions/13-api-sdk-agents.md)
