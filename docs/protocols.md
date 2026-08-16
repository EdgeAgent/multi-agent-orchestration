# Standardized Protocol Stack: MCP, ACP, A2A, and ANP

To replace brittle, ad-hoc integration code, the enterprise AI ecosystem has organized agent communications into a standardized four-layer protocol stack. This protocol stack establishes clear boundaries between model context interaction, internal agent messaging, cross-organizational delegation, and decentralized discovery.

The foundational layer is the Model Context Protocol (MCP), developed by Anthropic and governed under the Linux Foundation's Agentic AI Foundation. MCP standardizes interactions between language models and external tools, databases, or enterprise data sources using a robust JSON-RPC 2.0 client-server architecture operating over Server-Sent Events (SSE) or HTTP transports. 

For internal agent coordination, the Agent Communication Protocol (ACP), originated by IBM Research, provides a REST-native messaging framework designed specifically for seamless agent-to-agent communication over standard HTTP channels. When tasks require cross-organizational delegation, the Agent-to-Agent Protocol (A2A), spearheaded by Google Cloud alongside key enterprise partners, governs secure handoffs. Discovery within A2A relies on standardized Agent Cards hosted at RFC 8615 well-known endpoints (`/.well-known/agent.json`).

Finally, the Agent Network Protocol (ANP) provides a decentralized discovery and execution layer for open-internet agent networks. ANP leverages Decentralized Identifiers (DIDs) and JSON-LD knowledge graphs to establish trust, cryptographic verification, and state synchronization across independent agent collectives operating across distributed infrastructure.
