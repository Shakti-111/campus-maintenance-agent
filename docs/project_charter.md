# Campus Maintenance Resolution Agent

## Project status

Phase 1 - Problem validation

## Problem hypothesis

Campus maintenance complaints may be reported through disconnected channels.
This can cause incomplete information, duplicate complaints, incorrect routing,
missed follow-ups, and uncertain resolution status.

This problem statement will be updated after interviews with real users.

## Target users

- Students or staff reporting an issue
- Maintenance coordinator or hostel warden
- Maintenance technicians

## Proposed solution

A web-based system that collects structured complaints, identifies related cases,
recommends routing, tracks deadlines, drafts follow-up messages, and requests
human approval before important actions.

## Initial pilot scope

- One hostel or one academic building
- Plumbing, electrical, and housekeeping complaints
- Web application only
- Human approval required for assignment, escalation, and outgoing messages

## The system must not

- Make autonomous emergency decisions
- Replace emergency reporting channels
- Approve payments or purchases
- Evaluate technician performance
- Close a complaint without confirmation or authorized approval

## Initial success metrics

- Complaint registration time
- Percentage of complaints requiring clarification
- Routing accuracy
- Duplicate complaint detection accuracy
- Number of manual follow-ups
- Time until confirmed resolution
- Incorrect closure rate

## Development approach

1. Investigate the real problem.
2. Build a basic complaint-management system without AI.
3. Measure the baseline workflow.
4. Add bounded agentic capabilities.
5. Compare the AI-assisted system with the baseline.
6. Document limitations, safety controls, and results.
