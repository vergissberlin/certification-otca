# OTCA Training Exercises

This directory contains practical exercises for each topic covered in the OpenTelemetry Certified Associate (OTCA) exam. Each exercise file includes learning objectives, tasks, and references to relevant code in the system.

## Exercise Structure

Each exercise file contains:

- **Learning Objectives**: What you'll learn
- **Prerequisites**: What you need to know first
- **Exercise Tasks**: Practical hands-on tasks
- **Verification Steps**: How to verify your solution
- **Solution Reference**: Link to detailed solution

Solutions are provided in the [`solutions/`](./solutions/) directory.

## Fundamentals of Observability (18%)

1. [Telemetry Data](./01-fundamentals-telemetry-data.md)
   - Understand traces, metrics, and logs
   - Identify telemetry types in the system
   - Compare different telemetry signals

2. [Semantic Conventions](./02-fundamentals-semantic-conventions.md)
   - Learn OpenTelemetry semantic conventions
   - Add resource and span attributes
   - Apply conventions to improve observability

3. [Instrumentation](./03-fundamentals-instrumentation.md)
   - Understand automatic vs manual instrumentation
   - Add manual instrumentation
   - Combine both approaches

4. [Analysis and Outcomes](./04-fundamentals-analysis-outcomes.md)
   - Analyze trace data in Jaeger
   - Analyze metrics in Prometheus
   - Correlate traces and metrics
   - Identify issues from observability data

## The OpenTelemetry API and SDK (46%)

1. [Data Model](./05-api-sdk-data-model.md)
   - Understand spans, metrics, and resources
   - Create different metric types
   - Work with data model components

2. [Composability and Extension](./06-api-sdk-composability-extension.md)
   - Understand composable architecture
   - Modify processors and exporters
   - Create custom components

3. [Configuration](./07-api-sdk-configuration.md)
   - Configure via environment variables
   - Configure programmatically
   - Understand configuration precedence

4. [Signals: Tracing](./08-api-sdk-signals-tracing.md)
   - Create and manage spans
   - Add span attributes and events
   - Set span status
   - Create distributed traces

5. [Signals: Metrics](./09-api-sdk-signals-metrics.md)
   - Create different metric types
   - Add metric labels
   - Understand metric aggregation

6. [Signals: Logs](./10-api-sdk-signals-logs.md)
    - Understand log signal
    - Integrate logging with OpenTelemetry
    - Correlate logs with traces

7. [SDK Pipelines](./11-api-sdk-pipelines.md)
    - Understand trace and metrics pipelines
    - Modify pipeline configuration
    - Understand pipeline flow

8. [Context Propagation](./12-api-sdk-context-propagation.md)
    - Understand context propagation
    - Verify automatic propagation
    - Inspect trace context

9. [Agents](./13-api-sdk-agents.md)
    - Understand OpenTelemetry agents
    - Compare agent vs SDK approach
    - Identify agent-like components

## The OpenTelemetry Collector (26%)

1. [Collector Configuration](./14-collector-configuration.md)
    - Configure receivers, processors, exporters
    - Modify pipeline configuration
    - Understand configuration structure

2. [Collector Deployment](./15-collector-deployment.md)
    - Understand deployment options
    - Modify deployment configuration
    - Configure health checks

3. [Collector Scaling](./16-collector-scaling.md)
    - Understand scaling strategies
    - Configure horizontal scaling
    - Configure vertical scaling

4. [Collector Pipelines](./17-collector-pipelines.md)
    - Understand pipeline architecture
    - Modify pipeline components
    - Create multiple pipelines

5. [Transforming Data](./18-collector-transforming-data.md)
    - Understand data transformation
    - Add attributes processor
    - Use transform processor

## Maintaining and Debugging Observability Pipelines (10%)

1. [Debugging: Context Propagation](./19-debugging-context-propagation.md)
    - Debug context propagation issues
    - Verify propagation
    - Fix propagation problems

2. [Debugging: Pipelines](./20-debugging-pipelines.md)
    - Debug Collector pipeline issues
    - Use Collector logs
    - Verify pipeline configuration

3. [Debugging: Error Handling](./21-debugging-error-handling.md)
    - Understand error types
    - Debug export errors
    - Configure error handling

4. [Debugging: Schema Management](./22-debugging-schema-management.md)
    - Understand schema management
    - Debug schema compatibility
    - Handle schema evolution

## How to Use These Exercises

1. **Start with Fundamentals**: Begin with exercises 1-4 to build a solid foundation
2. **Work Through Systematically**: Follow the order, as later exercises build on earlier concepts
3. **Try Before Looking**: Attempt each exercise before checking the solution
4. **Verify Your Work**: Use the verification steps to ensure you've completed tasks correctly
5. **Review Solutions**: Check solutions for detailed explanations and best practices

## Prerequisites

Before starting the exercises:

- System is running (`docker-compose up`)
- Basic understanding of Docker and containers
- Access to Jaeger UI (<http://localhost:16686>)
- Access to Prometheus UI (<http://localhost:9090>)
- Basic knowledge of Node.js and Python (helpful but not required)

## Getting Help

- Check the [main README](../README.md) for system overview
- Review solution files in [`solutions/`](./solutions/) directory
- Consult OpenTelemetry documentation: <https://opentelemetry.io/docs/>

## Exam Preparation Tips

- Complete all exercises to cover all exam topics
- Focus on understanding concepts, not just memorizing
- Practice modifying the system to reinforce learning
- Use the exercises to identify areas needing more study
- Review solutions to understand best practices

Good luck with your OTCA exam preparation!
