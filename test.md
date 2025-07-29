Ubuntu Not Booting After Windows Update (Fresh System)

## 🔧 Fresh System Setup (No Preconditions)

### 1. Install Windows (10 or 11)
- Use **UEFI mode** (not Legacy BIOS).
- Allow Windows to create the **EFI System Partition (ESP)**.

### 2. Shrink Windows Partition
- Use **Disk Management** in Windows.
- Free up unallocated space for Ubuntu.

### 3. Install Ubuntu
- Boot from Ubuntu installation media in **UEFI mode**.
- Choose **"Install Ubuntu alongside Windows"** or use **manual partitioning**.
- Ensure **GRUB is installed to the EFI partition** (`/boot/efi`, usually `/dev/sda1`).
- This installs GRUB to: `/EFI/ubuntu/grubx64.efi`.

### 4. Reboot and Verify Dual Boot
- GRUB menu appears at startup.
- User can boot into **either Windows or Ubuntu**.

---

## 🔁 Triggering the Issue

### 5. Boot into Windows

### 6. Install Major Windows Update
- Apply a **Feature Update**, version upgrade (e.g., 22H2 → 23H2), or cumulative update.

### 7. Allow System to Reboot and Complete Update

---

## ❌ Post-Update Behavior

### 8. Reboot After Update
- **GRUB menu no longer appears**.
- System boots **directly into Windows**.

### 9. Attempt to Boot Ubuntu via UEFI Boot Menu
- Select "ubuntu" (if still listed).

### 10. Observe Error Message:
