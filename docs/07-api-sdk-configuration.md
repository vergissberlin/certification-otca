# Configuration

**Exam Weight**: The OpenTelemetry API and SDK (46%)

## Learning Objectives

- Understand OpenTelemetry configuration methods
- Learn environment variable configuration
- Learn programmatic configuration
- Understand configuration precedence
- Configure SDK components

## Prerequisites

- System is running
- Understanding of SDK components
- Basic knowledge of environment variables

## Exercise Tasks

### Task 1: Identify Configuration Methods

**Description**: Examine the system to identify all configuration methods in use.

**Expected Outcome**:

- Identify environment variable configuration
- Identify programmatic configuration
- Understand configuration sources
- Document configuration approach

**Hints**:

- Check `docker-compose.yaml` for environment variables
- Check service files for programmatic config
- Environment variables: `OTEL_*`
- Programmatic: code configuration

**Reference Files**:

- `docker-compose.yaml` (lines 12-15, 24-27)
- `service-node/app.js`
- `service-python/app.py`

### Task 2: Configure via Environment Variables

**Description**: Modify configuration using environment variables.

**Expected Outcome**:

- Add new environment variables
- Configure service name via environment
- Configure sampling via environment
- Understand environment variable format

**Hints**:

- Environment variables: `OTEL_SERVICE_NAME`, `OTEL_TRACES_SAMPLER`
- Modify `docker-compose.yaml`
- Restart services to apply changes
- Check OpenTelemetry environment variable spec

**Reference Files**:

- `docker-compose.yaml`
- OpenTelemetry environment variable documentation

### Task 3: Configure Programmatically

**Description**: Modify programmatic SDK configuration.

**Expected Outcome**:

- Modify TracerProvider configuration
- Modify MeterProvider configuration
- Configure resource attributes programmatically
- Understand programmatic options

**Hints**:

- Modify code in service files
- Configure providers with options
- Set resource attributes in code
- Programmatic config overrides environment

**Reference Files**:

- `service-node/app.js` (lines 12-14, 16-18)
- `service-python/app.py` (lines 13, 19-20)

### Task 4: Understand Configuration Precedence

**Description**: Understand which configuration takes precedence.

**Expected Outcome**:

- Understand environment vs programmatic precedence
- Test configuration precedence
- Document configuration order
- Know best practices

**Hints**:

- Programmatic usually overrides environment
- Some settings only available programmatically
- Environment variables for deployment flexibility
- Use appropriate method for use case

**Reference Files**:

- All configuration files
- OpenTelemetry configuration documentation

## Verification Steps

1. **Configuration Method Verification**:
   - Can you identify all configuration methods?
   - Understand when to use each?
   - Know configuration sources?

2. **Environment Variable Verification**:
   - Verify environment variables take effect
   - Check service behavior with new config
   - Understand variable format

3. **Programmatic Configuration Verification**:
   - Verify code changes take effect
   - Check configuration is applied
   - Understand programmatic options

4. **Precedence Verification**:
   - Understand which config wins
   - Test precedence behavior
   - Know best practices

## Solution

See [Solution: Configuration](../solutions/07-api-sdk-configuration.md)
