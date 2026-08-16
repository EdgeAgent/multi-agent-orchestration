import matplotlib.pyplot as plt
import numpy as np

# Set style
plt.style.use('seaborn-v0_8-darkgrid' if 'seaborn-v0_8-darkgrid' in plt.style.available else 'default')
fig, ax = plt.subplots(figsize=(10, 6), dpi=300)

topologies = ['Unstructured Peer', 'Shared Blackboard', 'Multi-Perspective Debate', 'Sequential Pipeline', 'Fan-Out / Fan-In', 'Hierarchical Supervisor']
multipliers = [15.0, 10.0, 3.2, 2.0, 1.5, 2.5]
colors = ['#ef4444', '#f97316', '#eab308', '#3b82f6', '#06b6d4', '#10b981']

bars = ax.barh(topologies, multipliers, color=colors, edgecolor='none', height=0.6)

ax.set_xlabel('Token Consumption Multiplier (vs Single Agent Baseline)', fontsize=12, fontweight='bold', labelpad=10)
ax.set_title('Multi-Agent Topology Token Inflation & Cost Multipliers', fontsize=14, fontweight='bold', pad=15)
ax.set_xlim(0, 18)

for bar in bars:
    width = bar.get_width()
    ax.text(width + 0.3, bar.get_y() + bar.get_height()/2, f'{width}x', 
            va='center', ha='left', fontsize=10, fontweight='bold', color='#1f2937')

plt.tight_layout()
plt.savefig('/home/ubuntu/multi-agent-orchestration/docs/token_inflation_chart.png')
plt.close()

# Chart 2: Failure Rate & Cost Risk
fig, ax = plt.subplots(figsize=(8, 5), dpi=300)
categories = ['Production Pilot Failures', 'Falsehood Cascade Rate', 'Runaway Cost Incidents']
rates = [40, 100, 25]  # percentages / severity indicators
colors_risk = ['#dc2626', '#991b1b', '#b91c1c']

bars = ax.bar(categories, rates, color=colors_risk, width=0.5)
ax.set_ylabel('Percentage / Risk Impact (%)', fontsize=12, fontweight='bold')
ax.set_title('Enterprise Multi-Agent Risk & Failure Vulnerabilities', fontsize=14, fontweight='bold', pad=15)
ax.set_ylim(0, 120)

for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height + 3, f'{height}%',
            ha='center', va='bottom', fontsize=11, fontweight='bold')

plt.tight_layout()
plt.savefig('/home/ubuntu/multi-agent-orchestration/docs/risk_metrics_chart.png')
plt.close()
print("Charts generated successfully.")
