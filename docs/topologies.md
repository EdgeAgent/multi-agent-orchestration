# Taxonomy of Multi-Agent Control Flow Patterns

Industrial multi-agent orchestration relies on six primary operational topologies, differentiated by their control-flow state, communication boundaries, and execution models.

---

## 1. Fan-Out / Fan-In (Parallel Scatter-Gather)

The Fan-Out / Fan-In topology dispatches a decomposed task simultaneously across $N$ specialized worker agents, aggregating their individual outputs through a collector node via LLM synthesis, weighted scoring, or deterministic voting.

### Operational Mechanics
- **Dispatcher Node:** Splits incoming tasks into parallel sub-tasks based on functional boundaries.
- **Worker Pool:** $N$ concurrent agents execute sub-tasks without inter-agent messaging latency.
- **Collector Node:** Aggregates outputs, performs deduplication, and resolves conflicts.

### Mathematical Race Condition Density
For a fan-out topology deploying $N$ parallel workers accessing shared resources, the potential state race condition density $C$ is defined by:
$$C = \frac{N(N - 1)}{2}$$
- 5 agents = 10 potential state conflict paths.
- 10 agents = 45 potential race conditions.

---

## 2. Sequential Pipeline (Assembly Line)

The Sequential Pipeline processes work through a linear, deterministic chain of specialized agents, where each stage consumes the intermediate output artifact of the preceding stage. Order is fixed at design time, making this topology suited for multi-stage document processing and regulatory compliance validation.

---

## 3. Multi-Perspective Debate

The Debate topology coordinates iterative, adversarial exchanges among specialized agents to refine complex strategic decisions. Exemplified by systems like Microsoft’s Copilot Council, this structure uses opposing agent personas (such as risk evaluators, macro analysts, and compliance reviewers) to systematically critique proposed outputs until reaching consensus or passing an evaluation gate.

---

## 4. Hierarchical Supervisor (Hub-and-Spoke)

The Hierarchical Supervisor topology serves as the standard design pattern for complex enterprise workflows. A central supervisor agent maintains the primary task state, decomposes incoming requests, dynamically routes subtasks to domain-specific worker agents, and compresses returned outputs into the global execution context.

### Asymmetric Model Routing
Organizations optimize cost structures within this topology by assigning high-level planning and routing to a frontier model (such as GPT-4o or Claude 3.5 Sonnet) while delegating specialized execution to lighter, domain-focused models (such as GPT-4o-mini or Claude 3.5 Haiku), yielding operational cost reductions of **40% to 60%** [1].

---

## 5. Bounded Peer Mesh and Swarms

The Bounded Peer Mesh pattern allows specialized agents to communicate across a shared workspace constrained by explicit phase gates, hidden selectors, and arbitration rules.

---

## 6. Shared Memory Blackboard (Hive)

In the Shared Memory Blackboard pattern, worker agents operate independently without direct peer-to-peer messaging dependencies. Instead, all agents read from and write to a common, versioned global state store.
