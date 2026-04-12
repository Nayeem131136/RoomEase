<div align="center">

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:00f5d4,50:1558b0,100:b14eff&height=220&section=header&text=RoomEase&fontSize=60&fontColor=ffffff&fontAlignY=38&desc=Smart%20Web-Based%20Classroom%20Booking%20System%20%F0%9F%8F%AB&descAlignY=58&descSize=18&animation=fadeIn"/>

<br/>

[![GitHub](https://img.shields.io/badge/🌐%20GitHub-RoomEase-00f5d4?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Nayeem131136/RoomEase)
&nbsp;
[![Django](https://img.shields.io/badge/Django%205.2-092E20?style=for-the-badge&logo=django&logoColor=white)](https://djangoproject.com)
&nbsp;
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
&nbsp;
[![UAP](https://img.shields.io/badge/UAP-CSE%20302-ffd60a?style=for-the-badge)](https://uap-bd.edu)

<br/>

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=18&pause=1000&color=00F5D4&center=true&vCenter=true&width=650&lines=Smart+Classroom+Booking+for+UAP+Students+%26+Faculty+%F0%9F%8F%AB;Real-Time+Availability+%26+AI-Based+Scheduling+%E2%9A%A1;Booking+Conflict+Detection+%26+Smart+Cancellation+%F0%9F%9A%AB;Built+with+Django+5.2+%7C+MVC+%7C+Django+Admin+%F0%9F%94%A5" alt="Typing SVG"/>

<br/><br/>

[![Top Contributor](https://img.shields.io/badge/🏆%20Top%20Contributor-7%20commits%20%7C%201%2C175%20lines-ff2d78?style=for-the-badge)](https://github.com/Nayeem131136/RoomEase)

</div>

---

## 📖 About

**RoomEase** is a smart web-based classroom booking system designed to optimize classroom utilization at the **University of Asia Pacific (UAP)**. It solves the problem of unused classrooms due to unexpected cancellations by providing real-time availability tracking, AI-based scheduling, and an intelligent booking system for both students and faculty.

> *"Eliminate empty classrooms. Maximize learning spaces. Simplify scheduling."*

---

## ✨ Key Features

<div align="center">

| Feature | Description |
|---|---|
| 📅 **Real-Time Availability** | Instantly check which rooms are free at any time slot |
| 🤖 **AI-Based Scheduling** | Smart suggestions to avoid conflicts and optimize space |
| 🔒 **Conflict Detection** | Automatically prevents double-booking of rooms |
| 👥 **Role-Based Access** | CR (Class Rep), Faculty, and Admin with separate permissions |
| ❌ **Smart Cancellation** | Cancel bookings with reason — room instantly freed |
| 🛠️ **Django Admin Panel** | Full room, time slot & booking approval management |
| 📊 **Daily Schedules** | View complete day-wise schedule for any room |
| ✅ **Booking Approval** | Admin approval workflow for booking requests |

</div>

---

## 🛠️ Tech Stack

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django%205.2-092E20?style=flat-square&logo=django&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=flat-square&logo=sqlite&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-7952B3?style=flat-square&logo=bootstrap&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)

</div>

---

## 🏗️ Project Structure (4 Modular Apps)

```
RoomEase/
├── 👤 accounts/           # User auth & role management
│   ├── models.py          # Extended User model (CR, Faculty, Admin)
│   ├── views.py           # Login, register, logout
│   └── urls.py
│
├── 🏫 classrooms/         # Room & time slot management
│   ├── models.py          # Room, TimeSlot, DailySchedule models
│   ├── views.py           # Dashboard, availability check
│   ├── admin.py           # Django Admin: Rooms, Slots, Schedules
│   └── urls.py
│
├── 📋 bookings/ (within classrooms)
│   ├── models.py          # BookingRequest model
│   ├── views.py           # Book, cancel, approve workflow
│   └── admin.py           # Booking approval in Admin
│
└── 🌐 templates/
    ├── accounts/          # Login, register pages
    └── classrooms/        # Dashboard, schedule, booking pages
```

---

## ⚙️ Installation & Setup

```bash
# 1. Clone the repository
git clone https://github.com/Nayeem131136/RoomEase.git
cd RoomEase

# 2. Install Django
pip install django

# 3. Apply migrations
python manage.py makemigrations
python manage.py migrate

# 4. Create superuser (Admin)
python manage.py createsuperuser

# 5. Run the server
python manage.py runserver
```

Then visit:
- **App:** `http://127.0.0.1:8000/user/login`
- **Admin:** `http://127.0.0.1:8000/admin`

---

## 🚦 How It Works

```
👤 User logs in (CR / Faculty)
        ↓
📅 Dashboard shows today's room schedule
        ↓
🟢 Available slots → Click "Book"
        ↓
📝 Enter booking reason → Submit Request
        ↓
🛠️ Admin approves in Django Admin panel
        ↓
✅ Room booked! Shown in daily schedule
        ↓
❌ Need to cancel? Click "Cancel" → Reason required → Room freed instantly
```

---

## 🖥️ Screenshots

| Dashboard | Booking | Admin Panel |
|---|---|---|
| Room availability with time slots | Book a room with reason | Approve/manage all bookings |
| Today's full schedule | Cancel with confirmation | Manage rooms & time slots |

---

## 📐 Class Diagram Highlights

```
User ──────────────── BookingRequest
 │  (FK: user)              │
 │                    (FK: room, timeslot)
 └─── Role: CR/Faculty      │
                       Classroom ──── TimeSlot
                             │              │
                       DailySchedule ───────┘
                       (day + course + room + slot)
```

**4 Core Models:**
- `User` — extended with role field (CR / Faculty)
- `Classroom` — room number, capacity, department
- `TimeSlot` — 7 slots (08:00–06:20)
- `BookingRequest` — user, room, day, slot, reason, status (Pending/Approved/Rejected)

---

## 📊 GitHub Contributions

<div align="center">

| Contributor | Commits | Lines Added | Lines Deleted |
|---|---|---|---|
| 🥇 **Nayeem131136 (Nayeem)** | **7** | **+1,175** | **-195** |
| 🥈 tandra136131 (Rupasha) | 4 | +465 | -41 |
| 🥉 Rifah03 (Rifah) | 3 | +274 | -14 |
| ankitahossain (Anushka) | 3 | +221 | -9 |

</div>

---

## 👥 Team

<div align="center">

| Name | ID | GitHub |
|---|---|---|
| **Md. Mahdi Hasan Nayeem** | 22201131 | [@Nayeem131136](https://github.com/Nayeem131136) |
| Rifah Tasfia | 22201126 | [@Rifah03](https://github.com/Rifah03) |
| Ankita Hossain Anushka | 22201130 | [@ankitahossain](https://github.com/ankitahossain) |
| Rupasha Khan Tandra | 22201136 | [@tandra136131](https://github.com/tandra136131) |

**Course:** CSE 302 — Object Oriented Programming II Lab: Visual and Web Design
**Instructor:** Durjoy Mistry, Lecturer, CSE — University of Asia Pacific
**Group:** RoomEase — Group 05

</div>

---

## 📦 Requirements

```txt
django==5.2
asgiref==3.8.1
sqlparse==0.5.3
tzdata==2025.2
```

---

<div align="center">

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:b14eff,50:1558b0,100:00f5d4&height=120&section=footer"/>

**⭐ Star this repo if it helped you!**

[![GitHub stars](https://img.shields.io/github/stars/Nayeem131136/RoomEase?style=social)](https://github.com/Nayeem131136/RoomEase/stargazers)
&nbsp;
[![GitHub forks](https://img.shields.io/github/forks/Nayeem131136/RoomEase?style=social)](https://github.com/Nayeem131136/RoomEase/network/members)

*Built with ❤️ for UAP | CSE 302 — University of Asia Pacific*

</div>
