import {
  LayoutDashboard,
  ClipboardList,
  PlusCircle,
  Bell,
  Bot,
  User,
  Building2,
  Briefcase,
} from "lucide-react";

export interface MenuItem {
  label: string;
  path: string;
  icon: React.ElementType;
}

export const sidebarMenus: Record<string, MenuItem[]> = {
  Citizen: [
    {
      label: "Dashboard",
      path: "/citizen/dashboard",
      icon: LayoutDashboard,
    },
    {
      label: "My Complaints",
      path: "/citizen/complaints",
      icon: ClipboardList,
    },
    {
      label: "Report Complaint",
      path: "/citizen/report",
      icon: PlusCircle,
    },
    {
      label: "Notifications",
      path: "/citizen/notifications",
      icon: Bell,
    },
    {
      label: "AI Assistant",
      path: "/citizen/chat",
      icon: Bot,
    },
    {
      label: "Profile",
      path: "/profile",
      icon: User,
    },
  ],

  "Municipal Officer": [
    {
      label: "Dashboard",
      path: "/municipal/dashboard",
      icon: LayoutDashboard,
    },
    {
      label: "Issues",
      path: "/municipal/complaints",
      icon: ClipboardList,
    },
    {
      label: "Departments",
      path: "/municipal/departments",
      icon: Building2,
    },
    {
      label: "Profile",
      path: "/profile",
      icon: User,
    },
  ],

  "Department Officer": [
    {
      label: "Dashboard",
      path: "/department/dashboard",
      icon: LayoutDashboard,
    },
    {
      label: "Assigned Issues",
      path: "/department/complaints",
      icon: Briefcase,
    },
    {
      label: "Profile",
      path: "/profile",
      icon: User,
    },
  ],
};