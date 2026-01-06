# Transforming Data

**Exam Weight**: The OpenTelemetry Collector (26%)

## Learning Objectives

- Understand data transformation in Collector
- Learn transformation processors
- Modify span attributes
- Modify metric attributes
- Understand transformation use cases

## Prerequisites

- System is running
- Understanding of Collector processors
- Access to `otel-config.yaml`

## Exercise Tasks

### Task 1: Understand Data Transformation

**Description**: Learn about data transformation capabilities.

**Expected Outcome**:

- Understand transformation concept
- Learn transformation processors
- Understand transformation use cases
- Know when to transform data

**Hints**:

- Transform data before export
- Use processors for transformation
- Common: attributes, resource, transform
- Transform for compliance or routing

**Reference Files**:

- OpenTelemetry Collector processors documentation
- Transformation processors guide

### Task 2: Add Attributes Processor

**Description**: Add attributes processor to modify span attributes.

**Expected Outcome**:

- Add attributes processor
- Configure attribute modifications
- Add or modify attributes
- Verify attribute changes

**Hints**:

- Attributes processor modifies attributes
- Can add, update, delete attributes
- Configure in processors section
- Add to pipeline

**Reference Files**:

- `otel-config.yaml`
- Attributes processor documentation

### Task 3: Add Resource Processor

**Description**: Add resource processor to modify resource attributes.

**Expected Outcome**:

- Add resource processor
- Configure resource modifications
- Add or modify resource attributes
- Verify resource changes

**Hints**:

- Resource processor modifies resources
- Can add resource attributes
- Useful for adding metadata
- Configure in processors section

**Reference Files**:

- `otel-config.yaml`
- Resource processor documentation

### Task 4: Use Transform Processor

**Description**: Use transform processor for complex transformations.

**Expected Outcome**:

- Add transform processor
- Configure transformations
- Transform span or metric data
- Verify transformations

**Hints**:

- Transform processor for complex transformations
- Uses OTTL (OpenTelemetry Transformation Language)
- Powerful transformation capabilities
- Configure transformations

**Reference Files**:

- `otel-config.yaml`
- Transform processor documentation
- OTTL documentation

## Verification Steps

1. **Transformation Understanding Verification**:
   - Understand transformation concept
   - Know transformation processors
   - Understand use cases

2. **Attributes Processor Verification**:
   - Verify attributes processor works
   - Check attribute modifications
   - Understand attribute transformation

3. **Resource Processor Verification**:
   - Verify resource processor works
   - Check resource modifications
   - Understand resource transformation

4. **Transform Processor Verification**:
   - Verify transform processor works
   - Check complex transformations
   - Understand OTTL

## Solution

See [Solution: Transforming Data](../solutions/18-collector-transforming-data.md)
