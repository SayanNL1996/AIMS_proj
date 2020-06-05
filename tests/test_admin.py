import unittest
import mock
from users.admin import Admin
from database_connection import DatabaseConnection
from query import Queries


class workerTest(unittest.TestCase):

    def setUp(self):
        self.admin = Admin()

    @mock.patch.object(Admin, 'admin_report_management')
    @mock.patch.object(Admin, 'show_complaints')
    @mock.patch.object(Admin, 'admin_supervisor_mgmnt')
    @mock.patch.object(Admin, 'admin_worker_mgmnt')
    @mock.patch('builtins.input')
    def test_worker_tasks(self, mock_input, mock_admin_worker_mgmnt, mock_admin_supervisor_mgmnt, mock_show_complaints,
                          mock_admin_report_management):
        # choice = 1
        mock_input.return_value = 1
        self.supervisor.supervisor_tasks()
        mock_admin_worker_mgmnt.assert_called_once()

        # choice = 2
        mock_input.return_value = 2
        self.supervisor.supervisor_tasks()
        mock_admin_supervisor_mgmnt.assert_called_once()

        # choice = 3
        mock_input.return_value = 3
        self.supervisor.supervisor_tasks()
        mock_show_complaints.assert_called_once()

        # choice = 4
        mock_input.return_value = 4
        self.supervisor.supervisor_tasks()
        mock_admin_report_management.assert_called_once()

    @mock.patch.object(Admin, 'admin_tasks')
    @mock.patch.object(Admin, 'assign_jobrole')
    @mock.patch.object(Admin, 'delete_worker')
    @mock.patch.object(Admin, 'show_reports')
    @mock.patch.object(Admin, 'show_allworkers')
    @mock.patch.object(Admin, 'create_worker')
    @mock.patch('builtins.input')
    def test_admin_worker_mgmnt(self, mock_input, mock_create_worker, mock_show_allworkers, mock_show_reports,
                                mock_delete_worker, mock_assign_jobrole, mock_admin_tasks):
        # choice = 1
        mock_input.return_value = 1
        self.admin.admin_worker_mgmnt()
        mock_create_worker.assert_called_once()

        # choice = 2
        mock_input.return_value = 2
        self.admin.admin_worker_mgmnt()
        mock_show_allworkers.assert_called_once()

        # choice = 3
        mock_input.return_value = 3
        self.admin.admin_worker_mgmnt()
        mock_show_reports.assert_called_once()

        # choice = 4
        mock_input.return_value = 4
        self.admin.admin_worker_mgmnt()
        mock_delete_worker.assert_called_once()

        # choice = 5
        mock_input.return_value = 5
        self.admin.admin_worker_mgmnt()
        mock_assign_jobrole.assert_called_once()

        # choice = 6
        mock_input.return_value = 6
        self.admin.admin_worker_mgmnt()
        mock_admin_tasks.assert_called_once()

    @mock.patch.object(Admin, "input_create_worker_data")
    @mock.patch.object(DatabaseConnection, "dbconnection")
    @mock.patch('builtins.input')
    def test_create_worker(self, mock_input, mock_dbconnection, mock_input_create_worker_data):
        mock_conn = mock.Mock()
        mock_cursor = mock.Mock()
        mock_dbconnection.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor
        mock_input.side_effect = ('rahul', 'abc@gmail.com', 'Abc@1')
        query = Queries.create.value
        mock_cursor.execute.assert_called_once_with(query.format('rahul', 'abc@gmail.com', 'Abc@1'))
        mock_input_create_worker_data.assert_called_once()

    @mock.patch.object(Admin, "admin_worker_mgmnt")
    @mock.patch.object(DatabaseConnection, "dbconnection")
    @mock.patch('builtins.input')
    def test_delete_worker(self, mock_input, mock_dbconnection, mock_admin_worker_mgmnt):
        mock_conn = mock.Mock()
        mock_cursor = mock.Mock()
        mock_dbconnection.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor
        self.admin.delete_worker_id == 123
        mock_cursor.execute.assert_called_once()
        mock_admin_worker_mgmnt.assert_called_once()

    @mock.patch.object(DatabaseConnection, "dbconnection")
    @mock.patch('builtins.input')
    def test_show_allworkers(self, mock_input, mock_dbconnection):
        mock_conn = mock.Mock()
        mock_cursor = mock.Mock()
        mock_dbconnection.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor
        data = [('1', 'rahul', 'rahul@gmail.com', 'xyz')]
        mock_cursor.execute.return_value = data
        mock_input.return_value = 1
        mock_input.assert_called_once()
        self.admin.show_allworkers()

    @mock.patch.object(DatabaseConnection, "dbconnection")
    @mock.patch('builtins.input')
    def test_show_unassigned_workers(self, mock_input, mock_dbconnection):
        mock_conn = mock.Mock()
        mock_cursor = mock.Mock()
        mock_dbconnection.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor
        data = [('1', 'rahul', 'rahul@gmail.com', 'xyz')]
        mock_cursor.execute.return_value = data
        mock_input.return_value = 1
        mock_input.assert_called_once()
        self.admin.show_unassigned_workers()

    @mock.patch.object(Admin, 'admin_tasks')
    @mock.patch.object(Admin, 'assign_supervisor')
    @mock.patch.object(Admin, 'delete_supervisor_team')
    @mock.patch.object(Admin, 'delete_supervisor')
    @mock.patch.object(Admin, 'create_report')
    @mock.patch.object(Admin, 'create_supervisorTeam')
    @mock.patch('builtins.input')
    def test_admin_supervisor_mgmnt(self, mock_input, mock_create_supervisorTeam, mock_create_report,
                                    mock_delete_supervisor,
                                    mock_delete_supervisor_team, mock_assign_supervisor, mock_admin_tasks):
        # choice = 1
        mock_input.return_value = 1
        self.admin.admin_supervisor_mgmnt()
        mock_create_supervisorTeam.assert_called_once()

        # choice = 2
        mock_input.return_value = 2
        self.admin.admin_supervisor_mgmnt()
        mock_create_report.assert_called_once()

        # choice = 3
        mock_input.return_value = 3
        self.admin.admin_supervisor_mgmnt()
        mock_delete_supervisor.assert_called_once()

        # choice = 4
        mock_input.return_value = 4
        self.admin.admin_supervisor_mgmnt()
        mock_delete_supervisor_team.assert_called_once()

        # choice = 5
        mock_input.return_value = 5
        self.admin.admin_supervisor_mgmnt()
        mock_assign_supervisor.assert_called_once()

        # choice = 6
        mock_input.return_value = 6
        self.admin.admin_supervisor_mgmnt()
        mock_admin_tasks.assert_called_once()

    @mock.patch.object(Admin, "admin_supervisor_mgmnt")
    @mock.patch.object(DatabaseConnection, "dbconnection")
    @mock.patch('builtins.input')
    def test_create_supervisorTeam(self, mock_input, mock_dbconnection, mock_admin_supervisor_mgmnt):
        mock_conn = mock.Mock()
        mock_cursor = mock.Mock()
        mock_dbconnection.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor
        mock_input.side_effect = ('1', 'rahul', 'abc@gmail.com', 'Abc@1')
        query = Queries.create.value
        mock_cursor.execute.assert_called_once_with(query.format('1', 'rahul', 'abc@gmail.com', 'Abc@1'))
        mock_admin_supervisor_mgmnt.assert_called_once()

    @mock.patch.object(Admin, "admin_supervisor_mgmnt")
    @mock.patch.object(DatabaseConnection, "dbconnection")
    @mock.patch('builtins.input')
    def test_delete_supervisor(self, mock_input, mock_dbconnection, mock_admin_supervisor_mgmnt):
        mock_conn = mock.Mock()
        mock_cursor = mock.Mock()
        mock_dbconnection.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor
        self.admin.delete_supervisor_id == 123
        mock_cursor.execute.assert_called_once()
        mock_admin_supervisor_mgmnt.assert_called_once()

    @mock.patch.object(Admin, "admin_supervisor_mgmnt")
    @mock.patch.object(DatabaseConnection, "dbconnection")
    @mock.patch('builtins.input')
    def test_show_allsupervisors(self, mock_input, mock_dbconnection, mock_admin_supervisor_mgmnt):
        mock_conn = mock.Mock()
        mock_cursor = mock.Mock()
        mock_dbconnection.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor
        self.admin.delete_supervisor_teamnumber_id == 123
        mock_cursor.execute.assert_called_once()
        mock_admin_supervisor_mgmnt.assert_called_once()

    @mock.patch.object(DatabaseConnection, "dbconnection")
    @mock.patch('builtins.input')
    def test_show_allsupervisors(self, mock_input, mock_dbconnection):
        mock_conn = mock.Mock()
        mock_cursor = mock.Mock()
        mock_dbconnection.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor
        data = [('1', 'rahul', 'rahul@gmail.com', 'none', '1')]
        mock_cursor.execute.return_value = data
        mock_input.return_value = 1
        mock_input.assert_called_once()
        self.admin.show_allsupervisors()

    @mock.patch.object(DatabaseConnection, "dbconnection")
    @mock.patch('builtins.input')
    def test_show_unassigned_supervisors(self, mock_input, mock_dbconnection):
        mock_conn = mock.Mock()
        mock_cursor = mock.Mock()
        mock_dbconnection.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor
        data = [('1', 'rahul', 'rahul@gmail.com', 'none', '1')]
        mock_cursor.execute.return_value = data
        mock_input.return_value = 1
        mock_input.assert_called_once()
        self.admin.show_unassigned_workers()

    @mock.patch.object(DatabaseConnection, "dbconnection")
    @mock.patch('builtins.input')
    def test_show_complaints(self, mock_input, mock_dbconnection):
        mock_conn = mock.Mock()
        mock_cursor = mock.Mock()
        mock_dbconnection.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor
        data = [('1', 'fire', 'xyz')]
        mock_cursor.execute.return_value = data
        mock_input.return_value = 1
        mock_input.assert_called_once()
        self.admin.show_complaints()

    @mock.patch.object(Admin, 'admin_tasks')
    @mock.patch.object(Admin, 'show_pending_reports')
    @mock.patch.object(Admin, 'show_rejected_reports')
    @mock.patch.object(Admin, 'show_approved_reports')
    @mock.patch.object(Admin, 'show_all_reports')
    @mock.patch('builtins.input')
    def test_admin_report_management(self, mock_input, mock_show_all_reports, mock_show_approved_reports,
                                     mock_show_rejected_reports,
                                     mock_show_pending_reports, mock_admin_tasks):
        # choice = 1
        mock_input.return_value = 1
        self.admin.admin_report_management()
        mock_show_all_reports.assert_called_once()

        # choice = 2
        mock_input.return_value = 2
        self.admin.admin_report_management()
        mock_show_approved_reports.assert_called_once()

        # choice = 3
        mock_input.return_value = 3
        self.admin.admin_report_management()
        mock_show_rejected_reports.assert_called_once()

        # choice = 4
        mock_input.return_value = 4
        self.admin.admin_report_management()
        mock_show_pending_reports.assert_called_once()

        # choice = 5
        mock_input.return_value = 5
        self.admin.admin_report_management()
        mock_admin_tasks.assert_called_once()

    @mock.patch.object(DatabaseConnection, "dbconnection")
    @mock.patch('builtins.input')
    def test_show_all_reports(self, mock_input, mock_dbconnection):
        mock_conn = mock.Mock()
        mock_cursor = mock.Mock()
        mock_dbconnection.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor
        data = [('1', '2', '1', 'fire', 'xyz', 'open', 'fire', 'xyz')]
        mock_cursor.execute.return_value = data
        mock_input.return_value = 1
        mock_input.assert_called_once()
        self.admin.show_all_reports()

    @mock.patch.object(DatabaseConnection, "dbconnection")
    @mock.patch('builtins.input')
    def test_show_approved_reports(self, mock_input, mock_dbconnection):
        mock_conn = mock.Mock()
        mock_cursor = mock.Mock()
        mock_dbconnection.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor
        data = [('1', '2', '1', 'fire', 'xyz', 'open', 'fire', 'xyz')]
        mock_cursor.execute.return_value = data
        mock_input.return_value = 1
        mock_input.assert_called_once()
        self.admin.show_approved_reports()

    @mock.patch.object(DatabaseConnection, "dbconnection")
    @mock.patch('builtins.input')
    def test_show_rejected_reports(self, mock_input, mock_dbconnection):
        mock_conn = mock.Mock()
        mock_cursor = mock.Mock()
        mock_dbconnection.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor
        data = [('1', '2', '1', 'fire', 'xyz', 'fire', 'xyz')]
        mock_cursor.execute.return_value = data
        mock_input.return_value = 1
        mock_input.assert_called_once()
        self.admin.show_rejected_reports()

    @mock.patch.object(DatabaseConnection, "dbconnection")
    @mock.patch('builtins.input')
    def test_show_pending_reports(self, mock_input, mock_dbconnection):
        mock_conn = mock.Mock()
        mock_cursor = mock.Mock()
        mock_dbconnection.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor
        data = [('1', '2', '1', 'fire', 'xyz', 'fire', 'xyz')]
        mock_cursor.execute.return_value = data
        mock_input.return_value = 1
        mock_input.assert_called_once()
        self.admin.show_pending_reports()


if __name__ == '__main__':
    unittest.main()
