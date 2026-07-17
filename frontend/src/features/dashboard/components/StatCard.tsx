import { type ReactNode } from "react";

interface StatCardProps {
  title: string;
  value: number;
  icon: ReactNode;
}

export default function StatCard({ title, value, icon }: StatCardProps) {
  return (
    <div className="rounded-lg border border-paper-200 bg-paper-50 p-6">
      <div className="flex items-center justify-between">
        <div>
          <p className="font-mono text-[11px] uppercase tracking-wider text-ink-400">
            {title}
          </p>
          <h2 className="mt-2 font-serif text-3xl font-semibold text-ink-900">
            {value}
          </h2>
        </div>

        <div className="rounded-full border border-gold-400/60 bg-navy-900 p-3 text-gold-300">
          {icon}
        </div>
      </div>
    </div>
  );
}