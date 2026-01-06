# Semantic Conventions

**Exam Weight**: Fundamentals of Observability (18%)

## Learning Objectives

- Understand OpenTelemetry semantic conventions
- Learn about resource attributes
- Learn about span attributes
- Apply semantic conventions to improve observability

## Prerequisites

- System is running
- Understanding of telemetry data (previous exercise)
- Access to Jaeger UI

## Exercise Tasks

### Task 1: Identify Existing Semantic Conventions

**Description**: Examine the system to find where semantic conventions are used.

**Expected Outcome**:

- Identify resource attributes in the code
- Identify span attributes added by instrumentation
- List the semantic conventions currently in use
- Understand automatic vs manual convention application

**Hints**:

- Check `service-python/app.py` for resource attributes
- Look at Jaeger UI span details for attributes
- Automatic instrumentation adds many conventions
- Resource attributes identify the service

**Reference Files**:

- `service-python/app.py` (line 13)
- `service-node/app.js`
- Jaeger UI span details

### Task 2: Add Resource Attributes

**Description**: Add additional resource attributes to identify services better.

**Expected Outcome**:

- Add `service.version` resource attribute to Python service
- Add `service.namespace` resource attribute
- Add `deployment.environment` resource attribute
- Verify attributes appear in traces

**Hints**:

- Modify the Resource creation in `service-python/app.py`
- Use the Resource API to add attributes
- Check Jaeger to see resource attributes in traces
- Resource attributes apply to all spans from that service

**Reference Files**:

- `service-python/app.py` (line 13)
- OpenTelemetry semantic conventions: <https://opentelemetry.io/docs/specs/semconv/>

### Task 3: Add Custom Span Attributes

**Description**: Add custom attributes to spans to provide more context.

**Expected Outcome**:

- Add custom attributes to the manual span in Python service
- Add attributes like `user.id`, `request.method`, `response.status`
- Understand when to use semantic conventions vs custom attributes
- Verify attributes in Jaeger

**Hints**:

- Modify the span creation in `service-python/app.py` (line 26)
- Use `span.set_attribute()` method
- Prefer semantic conventions when available
- Custom attributes for domain-specific data

**Reference Files**:

- `service-python/app.py` (line 26)
- OpenTelemetry semantic conventions documentation

### Task 4: Apply HTTP Semantic Conventions

**Description**: Ensure HTTP requests follow semantic conventions.

**Expected Outcome**:

- Verify automatic instrumentation applies HTTP conventions
- Understand what conventions are applied automatically
- Document the HTTP attributes you see in traces
- Know when manual attributes are needed

**Hints**:

- Express and Flask instrumentation add HTTP conventions automatically
- Check Jaeger for `http.method`, `http.route`, `http.status_code`
- Understand the difference between semantic and custom attributes

**Reference Files**:

- `service-node/app.js` (Express instrumentation)
- `service-python/app.py` (Flask instrumentation)
- Jaeger UI span attributes

## Verification Steps

1. **Resource Attributes Verification**:
   - Check Jaeger UI for resource attributes
   - Verify `service.name` is present
   - Verify newly added attributes appear

2. **Span Attributes Verification**:
   - Open a trace in Jaeger
   - Check span details for custom attributes
   - Verify attributes are correctly set

3. **Semantic Conventions Verification**:
   - Verify HTTP conventions are present
   - Check that conventions follow OpenTelemetry standards
   - Understand the difference between semantic and custom attributes

## Solution

See [Solution: Semantic Conventions](../solutions/02-fundamentals-semantic-conventions.md)
