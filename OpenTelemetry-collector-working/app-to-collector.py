from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

# Service name is required for most backends
resource = Resource(attributes={
    SERVICE_NAME: "service-open-tele"
})

provider = TracerProvider(resource=resource)
processor = BatchSpanProcessor(
    OTLPSpanExporter(endpoint="http://localhost:4317"))
provider.add_span_processor(processor)
trace.set_tracer_provider(provider)
tracer = trace.get_tracer("my.tracer.name")


def do_work():
    with tracer.start_as_current_span("open-tele-span") as span:
        # do some work that 'span' will track
        print("doing some work...")
        current_span = trace.get_current_span()

        current_span.add_event("Gonna try it!")

        # # Do the thing

        current_span.add_event("Did it!")


if __name__ == "__main__":
    do_work()
