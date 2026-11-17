# Paper / checklist modules → code

| Checklist / paper | Module | Notes |
|---|---|---|
| Perception | `dynahive/perception.py` | Session events, access, history. Stage mapping is local ATT&CK consolidation. |
| Planner | `dynahive/planner.py`, `frame_agents.Planner` | Reconstructs progress, uncertainty, outcomes; assigns Environment / Guidance / Review. |
| Environment Agent | `dynahive/environment.py`, `agents.generate_environment` | Host/service/file construction. Former name: Honey Agent / `honey_agent`. |
| Guidance Agent | `dynahive/guidance.py`, `guidance_search.py` | Paper Algorithm 1 (`K=6`, `b=3`): expand / assess-on-visible-prefix / deterministic FeasibleWholeChain / select. Former name: Trap Agent. |
| Path verifier | `dynahive/path_verifier.py`, `guidance_search.feasible_whole_chain` | Deterministic checks; no LLM. |
| Review Agent | `dynahive/review.py`, `review_loop.py` | Checks (i) consistency (ii) clue/credential/path (iii) exposed facts and fingerprints; repair budget `R=2`; block deploy if required checks still fail. |
| Deception | `dynahive/deception.py`, `compile.py`, `freeze.py` | Deploy reviewed configs; progressive freeze of exposed facts. |
| World / VFS | `dynahive/honeypot.py`, `vfs.py` | Executable decoy filesystem and services. |
| Live session | `dynahive/dynahive_live_session.py` | Artifact shell + constrained LLM fallback. |
| Coordinator | `dynahive/frame_agents.Coordinator` | Closed-loop step. Former name: `FrameController`. |

Old identifiers `honey_agent`, `trap_agent`, `anti_recon`, and `FrameController` remain as aliases so existing call sites keep working.
