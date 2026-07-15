from repositories.dashboard_repository import DashboardRepository


class DashboardService:

    @staticmethod
    def get_citizen_dashboard(
        citizen_id: int
    ):

        return DashboardRepository.get_citizen_dashboard(
            citizen_id
        )

    @staticmethod
    def get_municipal_dashboard():

        return DashboardRepository.get_municipal_dashboard()

    @staticmethod
    def get_department_dashboard(
        department_id: int
    ):

        return DashboardRepository.get_department_dashboard(
            department_id
        )