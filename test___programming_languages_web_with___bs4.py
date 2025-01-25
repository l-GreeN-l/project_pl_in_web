from cffi.backend_ctypes import long
import pytest


class TestProgrammingLanguagesWeb:

    def beauty_print(self,
                     check_popularity,
                     website,
                     popularity,
                     front,
                     back
                     ):
        """
            Yahoo (Frontend:JavaScript | Backend:PHP) has 750000000
                    unique visitors per month.(Expected more than 500000)
        """

        return '\n' + (f'{website} (Frontend:{front} | Backend:{back}) has {str(popularity)} '
                       f'unique visitors per month.(Expected more than {long(check_popularity)})') + '\n'

    @pytest.mark.parametrize(
        "check_popularity", [
            10 ** 7,
            1.5 * 10 ** 7,
            5 * 10 ** 7,
            10 ** 8,
            5 * 10 ** 8,
            10 ** 9,
            1.5 * 10 ** 9
        ]
    )
    def test_size_popularity(self, check_popularity, Websites):
        """
            Websites
            Popularity(unique visitors per month)[1]
            Front-end(Client-side)
            Back-end(Server-side)
            Database
            Notes

        """
        trigger = False
        errors = []
        for item in Websites:

            if item.popularity < check_popularity:
                trigger = True
                message = self.beauty_print(
                    check_popularity=check_popularity,
                    popularity=item.popularity,
                    website=item.website,
                    front=item.frontend,
                    back=item.backend
                )
                errors.append(message)

        if trigger:
            raise AssertionError(''.join(errors))

