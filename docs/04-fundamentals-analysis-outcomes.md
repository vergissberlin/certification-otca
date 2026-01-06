# Analysis and Outcomes

**Exam Weight**: Fundamentals of Observability (18%)

## Learning Objectives

- Understand how to analyze telemetry data
- Learn to use observability backends (Jaeger, Prometheus)
- Interpret trace data for debugging
- Interpret metrics for performance analysis
- Understand observability outcomes and value

## Prerequisites

- System is running
- Understanding of traces and metrics
- Access to Jaeger UI and Prometheus UI
- Some telemetry data generated

## Exercise Tasks

### Task 1: Analyze Trace Data in Jaeger

**Description**: Use Jaeger UI to analyze trace data and answer questions about system behavior.

**Expected Outcome**:

- Find traces for specific services
- Identify slow operations from trace data
- Understand span timing and relationships
- Answer questions like "What took the longest?" and "Where did time go?"

**Hints**:

- Use Jaeger search to filter traces
- Look at trace timeline view
- Examine span durations
- Check for errors in spans

**Reference Files**:

- Jaeger UI (<http://localhost:16686>)
- Generated traces from services

### Task 2: Analyze Metrics in Prometheus

**Description**: Use Prometheus to query and analyze metrics.

**Expected Outcome**:

- Write PromQL queries for metrics
- Calculate request rates
- Understand metric aggregation
- Create simple visualizations

**Hints**:

- Query: `requests_total`
- Use `rate()` function for rates
- Use `sum()` for aggregation
- Try different time ranges

**Reference Files**:

- Prometheus UI (<http://localhost:9090>)
- `prometheus.yml`

### Task 3: Correlate Traces and Metrics

**Description**: Use both traces and metrics together to understand system behavior.

**Expected Outcome**:

- Correlate high metric values with trace patterns
- Understand when to use traces vs metrics
- Answer questions requiring both data types
- Create a correlation analysis

**Hints**:

- High request count (metric) should correlate with many traces
- Slow traces might indicate performance issues
- Use both to get complete picture
- Consider what each tells you

**Reference Files**:

- Jaeger UI and Prometheus UI
- Both telemetry types

### Task 4: Identify Issues from Observability Data

**Description**: Use observability data to identify and diagnose issues.

**Expected Outcome**:

- Identify performance bottlenecks
- Find error patterns
- Understand system behavior under load
- Create a report of findings

**Hints**:

- Look for long-duration spans
- Check for error status codes
- Examine metric trends
- Correlate patterns across services

**Reference Files**:

- All observability backends
- System logs if needed

## Verification Steps

1. **Trace Analysis Verification**:
   - Can you identify the slowest operation?
   - Can you see the complete request flow?
   - Can you identify where errors occur?

2. **Metrics Analysis Verification**:
   - Can you calculate request rate?
   - Can you see trends over time?
   - Can you aggregate metrics correctly?

3. **Correlation Verification**:
   - Can you use both traces and metrics together?
   - Do you understand when to use each?
   - Can you answer complex questions?

4. **Issue Identification Verification**:
   - Can you find performance issues?
   - Can you identify error patterns?
   - Can you provide actionable insights?

## Solution

See [Solution: Analysis and Outcomes](../solutions/04-fundamentals-analysis-outcomes.md)
