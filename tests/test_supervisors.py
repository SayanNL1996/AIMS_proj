import unittest
import mock
from users.supervisors import Supervisor
from database_connection import DatabaseConnection
from query import Queries

class workerTest(unittest.TestCase):

    def setUp(self):
        self.supervisor = Supervisor()

    @mock.patch.object(Supervisor, 'show_reports')
    @mock.patch.object(Supervisor, 'create_report')
    @mock.patch.object(Supervisor, 'show_complaint')
    @mock.patch('builtins.input')
    def test_supervisor_tasks(self, mock_input, mock_show_complaint, mock_create_report,
                          mock_show_reports):
        # choice = 1
        mock_input.return_value = 1
        self.supervisor.supervisor_tasks()
        mock_show_complaint.assert_called_once()

        # choice = 2
        mock_input.return_value = 2
        self.supervisor.supervisor_tasks()
        mock_create_report.assert_called_once()

        # choice = 3
        mock_input.return_value = 3
        self.supervisor.supervisor_tasks()
        mock_show_reports.assert_called_once()

        # choice = 4
        mock_input.return_value = 4
        self.supervisor.supervisor_tasks()
        self.assertRaises(Exception, 4)

    @mock.patch.object(DatabaseConnection, "dbconnection")
    @mock.patch('builtins.input')
    def test_show_complaint(self,mock_input,mock_dbconnection):
        mock_conn = mock.Mock()
        mock_cursor = mock.Mock()
        mock_dbconnection.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor
        data = [('fire','xyz','1')]
        mock_cursor.execute.return_value = data
        mock_input.return_value = 1
        mock_input.assert_called_once()
        self.supervisor.show_complaint()

    @mock.patch.object(Supervisor, "supervisor_tasks")
    @mock.patch.object(DatabaseConnection, "dbconnection")
    @mock.patch('builtins.input')
    def test_create_complaint(self, mock_input, mock_dbconnection, mock_supervisor_tasks):
        mock_conn = mock.Mock()
        mock_cursor = mock.Mock()
        mock_dbconnection.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor
        mock_input.side_effect = ('fire breakout', 'abc')
        query = Queries.create.value
        mock_cursor.execute.assert_called_once_with(query.format('fire breakout', 'abc'))
        mock_supervisor_tasks.assert_called_once()



    @mock.patch.object(DatabaseConnection, "dbconnection")
    @mock.patch('builtins.input')
    def test_show_reports(self, mock_input, mock_dbconnection):
        mock_conn = mock.Mock()
        mock_cursor = mock.Mock()
        mock_dbconnection.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor
        data = [('1','1','fire', 'xyz', '10')]
        mock_cursor.execute.return_value = data
        mock_input.return_value = 1
        mock_input.assert_called_once()
        self.supervisor.show_reports()



if __name__ == '__main__':
    unittest.main()






