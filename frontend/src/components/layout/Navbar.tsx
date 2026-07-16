import { Menu, Bell } from "lucide-react";

import { useAuth } from "../../hooks/useAuth";

interface NavbarProps {
  onMenuClick: () => void;
}

export default function Navbar({ onMenuClick }: NavbarProps) {
  const { user } = useAuth();

  return (
    <header className="sticky top-0 z-30 flex h-16 items-center justify-between border-b border-paper-200 bg-paper-50 px-6">
      <div className="flex items-center gap-4">
        <button
          onClick={onMenuClick}
          className="rounded-md p-2 text-ink-600 hover:bg-paper-200 lg:hidden"
        >
          <Menu size={22} />
        </button>

        <div>
          <h1 className="font-serif text-lg font-semibold text-ink-900">
            Dashboard
          </h1>
          <p className="font-mono text-[11px] uppercase tracking-wider text-ink-400">
            Welcome back
          </p>
        </div>
      </div>

      <div className="flex items-center gap-5">
        <button className="relative rounded-md p-2 text-ink-600 hover:bg-paper-200">
          <Bell size={20} strokeWidth={1.75} />
          <span className="absolute right-1.5 top-1.5 h-2 w-2 rounded-full bg-gold-500" />
        </button>

        <div className="flex items-center gap-3 border-l border-paper-200 pl-5">
          <div className="text-right">
            <p className="text-sm font-medium text-ink-900">
              {user?.full_name}
            </p>
            <p className="font-mono text-[11px] uppercase tracking-wider text-ink-400">
              {user?.role}
            </p>
          </div>
        </div>
      </div>
    </header>
  );
}