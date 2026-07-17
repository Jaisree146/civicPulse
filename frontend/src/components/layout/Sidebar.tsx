import { NavLink, useNavigate } from "react-router-dom";
import { LogOut, X, Landmark } from "lucide-react";

import { sidebarMenus } from "../../constants/sidebarMenu";
import { useAuth } from "../../hooks/useAuth";
import { useLogout } from "../../features/auth/hooks";

interface SidebarProps {
  isOpen: boolean;
  onClose: () => void;
}

export default function Sidebar({ isOpen, onClose }: SidebarProps) {
  const navigate = useNavigate();

  const { user, logout } = useAuth();

  const logoutMutation = useLogout();

  const menuItems = sidebarMenus[user?.role ?? "Citizen"] ?? [];

  const handleLogout = async () => {
    try {
      await logoutMutation.mutateAsync();
      logout();
      navigate("/login");
    } catch {
      logout();
      navigate("/login");
    }
  };

  return (
    <>
      {/* Mobile Overlay */}
      {isOpen && (
        <div
          onClick={onClose}
          className="fixed inset-0 z-40 bg-navy-950/50 lg:hidden"
        />
      )}

      {/* Sidebar */}
      <aside
        className={`
          fixed left-0 top-0 z-50
          flex h-screen w-64 flex-col
          border-r border-navy-800 bg-navy-900
          transition-transform duration-300

          ${isOpen ? "translate-x-0" : "-translate-x-full"}

          lg:static
          lg:translate-x-0
        `}
      >
        {/* Logo */}
        <div className="flex items-center justify-between border-b border-navy-800 p-5">
          <div className="flex items-center gap-3">
            <div className="flex h-9 w-9 shrink-0 items-center justify-center rounded-full border border-gold-400 text-gold-300">
              <Landmark size={16} strokeWidth={1.75} />
            </div>
            <div>
              <h1 className="font-serif text-lg font-semibold leading-tight text-paper-50">
                CivicPulse
              </h1>
              <p className="mt-0.5 font-mono text-[10px] uppercase tracking-wider text-gold-400/80">
                {user?.role}
              </p>
            </div>
          </div>

          <button
            onClick={onClose}
            className="text-paper-100/60 hover:text-paper-50 lg:hidden"
          >
            <X size={20} />
          </button>
        </div>

        {/* Navigation */}
        <nav className="flex-1 space-y-1 p-3">
          {menuItems.map((item) => {
            const Icon = item.icon;

            return (
              <NavLink
                key={item.path}
                to={item.path}
                onClick={onClose}
                className={({ isActive }) =>
                  `flex items-center gap-3 rounded-md border-l-2 px-3.5 py-2.5 text-sm transition-colors ${
                    isActive
                      ? "border-gold-500 bg-gold-500/10 text-gold-300"
                      : "border-transparent text-paper-100/70 hover:bg-navy-800 hover:text-paper-50"
                  }`
                }
              >
                <Icon size={18} strokeWidth={1.75} />
                <span>{item.label}</span>
              </NavLink>
            );
          })}
        </nav>

        {/* Footer */}
        <div className="border-t border-navy-800 p-3">
          <button
            onClick={handleLogout}
            disabled={logoutMutation.isPending}
            className="flex w-full items-center gap-3 rounded-md px-3.5 py-2.5 text-sm text-[#e0a3a3] transition-colors hover:bg-[#a13a3a]/15 hover:text-[#f2c4c4] disabled:opacity-60"
          >
            <LogOut size={18} strokeWidth={1.75} />
            {logoutMutation.isPending ? "Logging out…" : "Logout"}
          </button>
        </div>
      </aside>
    </>
  );
}