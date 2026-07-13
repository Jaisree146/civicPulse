from flask import g

from common.api_response import ApiResponse
from services.dashboard_service import DashboardService


class DashboardController:

    @staticmethod
    def citizen_dashboard():

        dashboard = DashboardService.get_citizen_dashboard(g.current_user.id)

        return ApiResponse.success(
            message="Citizen dashboard fetched successfully.",
            data=dashboard
        )

    @staticmethod
    def municipal_dashboard():

        dashboard = DashboardService.get_municipal_dashboard()

        return ApiResponse.success(
            message="Municipal dashboard fetched successfully.",
            data=dashboard
        )

    @staticmethod
    def department_dashboard():

        dashboard = DashboardService.get_department_dashboard(g.current_user.department_id)

        return ApiResponse.success(
            message="Department dashboard fetched successfully.",
            data=dashboard
        )