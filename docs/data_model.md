# Campus Maintenance Resolution Agent — Data Model

## 1. Complaint

A complaint represents a maintenance issue reported by a student or staff member.

| Field | Type | Required | Description |
|---|---|---:|---|
| id | Integer | Yes | Unique complaint identifier |
| title | String | Yes | Short description of the issue |
| description | Text | Yes | Detailed explanation of the problem |
| category | String | Yes | Plumbing, electrical, or housekeeping |
| location | String | Yes | Building, hostel, room, floor, or area |
| priority | String | Yes | Low, medium, high, or emergency-review |
| status | String | Yes | Submitted, under-review, assigned, in-progress, resolved, reopened, or closed |
| reporter_name | String | Yes | Name of the person reporting the issue |
| reporter_contact | String | Yes | Contact information for follow-up |
| assigned_to | String | No | Technician or maintenance team |
| created_at | DateTime | Yes | Time when the complaint was submitted |
| updated_at | DateTime | Yes | Time when the complaint was last updated |
| due_at | DateTime | No | Expected resolution deadline |
| resolution_notes | Text | No | Explanation of the repair or action taken |
| resolution_confirmed | Boolean | Yes | Whether an authorized person confirmed the resolution |

## 2. Complaint status workflow

```text
submitted
    ↓
under-review
    ↓
assigned
    ↓
in-progress
    ↓
resolved
    ↓
closed

## 3.MVP user identity decision

The MVP will represent users with the following roles:

- reporter
- coordinator
- technician
- administrator

During the first database implementation, complaint records may temporarily store
reporter and technician references as simple values. A dedicated users table will
be introduced before authentication and role-based access control are implemented.

The system must expose reporter contact information only to authorized users.
