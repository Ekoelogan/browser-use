from types import SimpleNamespace
from unittest.mock import AsyncMock

import pytest

from browser_use.browser.session import BrowserSession


@pytest.mark.asyncio
async def test_cookies_uses_supported_cdp_network_commands_import() -> None:
	cookies = [{'name': 'session', 'value': 'test-value'}]
	get_cookies = AsyncMock(return_value={'cookies': cookies})
	session = SimpleNamespace(
		cdp_client=SimpleNamespace(
			send=SimpleNamespace(Network=SimpleNamespace(getCookies=get_cookies)),
		)
	)

	result = await BrowserSession.cookies(session, ['https://example.com'])

	assert result == cookies
	get_cookies.assert_awaited_once_with({'urls': ['https://example.com']})
