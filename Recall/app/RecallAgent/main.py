from bedrock_agentcore.runtime import BedrockAgentCoreApp
from graph import build_graph

app = BedrockAgentCoreApp()

graph = build_graph()


@app.entrypoint
async def invoke(payload, context):
    result = await graph.ainvoke(payload)

    return {
        "result": result
    }


if __name__ == "__main__":
    app.run()