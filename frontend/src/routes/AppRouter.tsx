import { createBrowserRouter, Navigate } from "react-router-dom";

import Login from "../features/auth/Login";
import Register from "../features/auth/Register";

import ProtectedRoute from "./ProtectedRoute";
import RoleRoute from "./RoleRoute";

import DashboardLayout from "../layouts/DashboardLayout";

import CitizenDashboard from "../features/dashboard/citizen/Dashboard";
import MunicipalDashboard from "../features/dashboard/municipal/Dashboard";
import DepartmentDashboard from "../features/dashboard/department/Dashboard";

import MyComplaints from "../features/complaints/citizen/MyComplaints";
import ReportComplaint from "../features/complaints/citizen/ReportComplaint";
import ComplaintDetails from "../features/complaints/citizen/ComplaintDetails";

import PendingIssues from "../features/issues/municipal/PendingIssues";
import MunicipalIssueDetails from "../features/issues/municipal/IssueDetails";

import AssignedIssues from "../features/issues/departments/AssignedIssues";
import DepartmentIssueDetails from "../features/issues/departments/IssueDetails";

import Departments from "../features/issues/municipal/Departments";
import DepartmentIssues from "../features/issues/municipal/DepartmentIssues";

function Unauthorized() {
  return <h1>Unauthorized</h1>;
}

export const router = createBrowserRouter([
  {
    path: "/",
    element: <Navigate to="/login" replace />,
  },

  {
    path: "/login",
    element: <Login />,
  },

  {
    path: "/register",
    element: <Register />,
  },

  {
    element: <ProtectedRoute />,
    children: [
      {
        element: <DashboardLayout />,
        children: [


          {
            element: (
              <RoleRoute allowedRoles={["Citizen"]} />
            ),
            children: [
              {
                path: "/citizen/dashboard",
                element: <CitizenDashboard />,
              },
              {
                path: "/citizen/complaints",
                element: <MyComplaints />,
              },
              {
                path: "/citizen/complaints/new",
                element: <ReportComplaint />,
              },
              {
                path: "/citizen/complaints/:complaintNumber",
                element: <ComplaintDetails />,
              },
            ],
          },

         

          {
            element: (
              <RoleRoute
                allowedRoles={["Municipal Officer"]}
              />
            ),
            children: [
              {
                path: "/municipal/dashboard",
                element: <MunicipalDashboard />,
              },
              {
                path: "/municipal/issues",
                element: <PendingIssues />,
              },
              {
                path: "/municipal/issues/:issueNumber",
                element: <MunicipalIssueDetails />,
              },
                  
              {
                path: "/municipal/departments",
                element: <Departments />,
              },
              {   
              path: "/municipal/departments/:departmentId",
              element: <DepartmentIssues />,
                },
            ],
          },

          
          {
            element: (
              <RoleRoute
                allowedRoles={["Department Officer"]}
              />
            ),
            children: [
              {
                path: "/department/dashboard",
                element: <DepartmentDashboard />,
              },
              {
                path: "/department/issues",
                element: <AssignedIssues />,
              },
              {
                path: "/department/issues/:issueNumber",
                element: <DepartmentIssueDetails />,
              },
            ],
          },

        ],
      },
    ],
  },

  {
    path: "/unauthorized",
    element: <Unauthorized />,
  },
]);