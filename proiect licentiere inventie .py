"""
Inventii la colt de strada! - Tokenized License & Project Registry
------------------------------------------------------------------
Simulates the registration of open-source or tokenized inventions, 
manages investor funding milestones, and tracks licensing token yields.
"""

import time
from dataclasses import dataclass, field
from typing import Dict, List

@dataclass
class InventionProject:
    invention_id: str
    creator_name: str
    title: str
    category: str
    is_open_source: bool
    tokenized_valuation_eur: float
    tokens_issued: int
    funding_raised_eur: float = 0.0

class InnovationRegistrySystem:
    def __init__(self):
        self.projects: Dict[str, InventionProject] = {}
        self.total_platform_funding: float = 0.0

    def register_invention(self, inv_id: str, creator: str, title: str, category: str, open_source: bool, valuation: float, tokens: int) -> InventionProject:
        """Registers a new invention into the dual platform (Open Source or Tokenized)."""
        project = InventionProject(
            invention_id=inv_id,
            creator_name=creator,
            title=title,
            category=category,
            is_open_source=open_source,
            tokenized_valuation_eur=valuation,
            tokens_issued=tokens
        )
        self.projects[inv_id] = project
        print(f"[REGISTRY] Invention registered successfully: '{title}' (ID: {inv_id})")
        return project

    def invest_in_invention(self, inv_id: str, investment_amount_eur: float):
        """Allows investors/supporters to buy license tokens or fund the invention."""
        if inv_id in self.projects:
            proj = self.projects[inv_id]
            proj.funding_raised_eur += investment_amount_eur
            self.total_platform_funding += investment_amount_eur
            print(f"[INVESTMENT] €{investment_amount_eur:,.2f} invested in '{proj.title}' (Total Raised: €{proj.funding_raised_eur:,.2f})")
        else:
            print(f"[ERROR] Invention ID {inv_id} not found.")

    def generate_platform_summary(self):
        """Generates an executive summary of registered projects and funds."""
        print("\n" + "="*60)
        print("    'INVENTII LA COLT DE STRADA!' - PLATFORM SUMMARY")
        print("="*60)
        print(f"Total Registered Inventions: {len(self.projects)}")
        print(f"Total Platform Capital Raised: €{self.total_platform_funding:,.2f}")
        print("-" * 60)
        for pid, proj in self.projects.items():
            mode = "Open Source (Free)" if proj.is_open_source else "Tokenized License (RWA)"
            print(f" - [{pid}] {proj.title} by {proj.creator_name}")
            print(f"   Mode: {mode} | Valuation: €{proj.tokenized_valuation_eur:,.2f} | Raised: €{proj.funding_raised_eur:,.2f}")
        print("="*60)

# --- EXECUTION DEMO ---
if __name__ == "__main__":
    registry = InnovationRegistrySystem()

    # 1. Register an Open Source project (e.g., School AI Safety / Modular Infrastructure)
    registry.register_invention(
        inv_id="INV-001",
        creator="Marcel",
        title="Global AI School Safety & Modular Reintegration Hub",
        category="Infrastructură & Educație",
        open_source=True,
        valuation=50000.0,
        tokens=5000
    )

    # 2. Register a Tokenized Innovation project
    registry.register_invention(
        inv_id="INV-002",
        creator="Echipa Core",
        title="Smart RWA License & Automated Escrow Protocol",
        category="Web3 & Smart Contracts",
        open_source=False,
        valuation=120000.0,
        tokens=12000
    )

    # 3. Simulate investor funding matching Year 1 objectives (e.g., targeting initial development)
    registry.invest_in_invention("INV-001", 15000.0)
    registry.invest_in_invention("INV-002", 35000.0)

    # 4. Display Platform Status Report
    registry.generate_platform_summary()
