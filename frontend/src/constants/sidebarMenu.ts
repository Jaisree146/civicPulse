import { MessageCircle } from "lucide-react";
import {
  LayoutDashboard,
  ClipboardList,
  PlusCircle,
  Bell,
  Bot,
  User,
  Building2,
  Briefcase,
  UserCircle,
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
      path: "/citizen/complaints/new",
      icon: PlusCircle,
    },
    {
      label: "AI Assistant",
      path: "/citizen/chat",
      icon: Bot,
    },
    {
      label: "Profile",
      path: "/citizen/profile",
      icon: UserCircle,
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
      path: "/municipal/issues",
      icon: ClipboardList,
    },
    {
      label: "Departments",
      path: "/municipal/departments",
      icon: Building2,
    },
    {
      label: "Profile",
      path: "/municipal/profile",
      icon: UserCircle,
    },
    {
      label: "AI Assistant",
      path: "/citizen/chat",
      icon: MessageCircle,
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
      path: "/department/issues",
      icon: Briefcase,
    },
    {
      label: "Profile",
      path: "/department/profile",
      icon: UserCircle,
    },
  ],
};
