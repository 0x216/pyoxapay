import aiohttp
from aiohttp import ClientError

class OxaPayAPI:
    """
    A Python client for interacting with the OxaPay API.

    This class provides methods to interact with various OxaPay API endpoints
    asynchronously using aiohttp.

    Attributes:
        merchant_api_key (str): Your merchant API key for OxaPay.
    """

    def __init__(self, merchant_api_key):
        """
        Initializes the OxaPayAPI class with the merchant API key.

        Args:
            merchant_api_key (str): The merchant API key for authentication.
        """
        self.base_url = "https://api.oxapay.com"
        self.merchant_api_key = merchant_api_key
        self.session = aiohttp.ClientSession()

    async def create_invoice(self, **kwargs):
        """
        Creates a new invoice.

        Args:
            **kwargs: Arbitrary keyword arguments including:
                amount (float): The amount for the payment.
                currency (str): The currency for the invoice.
                lifeTime (int): Expiration time in minutes.
                feePaidByPayer (int): Who pays the fee (0 or 1).
                underPaidCover (float): Acceptable inaccuracy in payment.
                callbackUrl (str): URL for payment notifications.
                returnUrl (str): URL for redirection after payment.
                description (str): Order description.
                orderId (str): Unique order ID.
                email (str): Customer's email.

        Returns:
            dict: Response from the API.

        Raises:
            Exception: If the request fails.
        """
        url = f"{self.base_url}/merchants/request"
        data = {"merchant": self.merchant_api_key, **kwargs}
        try:
            async with self.session.post(url, json=data) as response:
                return await response.json()
            except ClientError as e:
                raise Exception(f"Failed to create invoice: {e}")

    async def create_static_wallet(self, currency, callbackUrl):
        """
        Creates a static wallet address for a specific currency.

        Args:
            currency (str): The currency for the static wallet.
            callbackUrl (str): URL for payment notifications.

        Returns:
            dict: Response from the API.

        Raises:
            Exception: If the request fails.
        """
        url = f"{self.base_url}/merchants/request/staticaddress"
        data = {
            "merchant": self.merchant_api_key,
            "currency": currency,
            "callbackUrl": callbackUrl
        }
        try:
            async with self.session.post(url, json=data) as response:
                return await response.json()
            except ClientError as e:
                raise Exception(f"Failed to create static wallet: {e}")

    async def revoke_static_wallet(self, address):
        """
        Revokes a static wallet by its address.

        Args:
            address (str): The address of the static wallet to revoke.

        Returns:
            dict: Response from the API.

        Raises:
            Exception: If the request fails.
        """
        url = f"{self.base_url}/merchants/revoke/staticaddress"
        data = {
            "merchant": self.merchant_api_key,
            "address": address
        }
        try:
            async with self.session.post(url, json=data) as response:
                return await response.json()
            except ClientError as e:
                raise Exception(f"Failed to revoke static wallet: {e}")

    async def get_payment_information(self, trackId):
        """
        Retrieves payment information by its TrackId.

        Args:
            trackId (int): The unique identifier for the payment session.

        Returns:
            dict: Response from the API.

        Raises:
            Exception: If the request fails.
        """
        url = f"{self.base_url}/merchants/inquiry"
        data = {
            "merchant": self.merchant_api_key,
            "trackId": trackId
        }
        try:
            async with self.session.post(url, json=data) as response:
                return await response.json()
            except ClientError as e:
                raise Exception(f"Failed to get payment information: {e}")

    async def close(self):
        """
        Closes the aiohttp session.

        Call this method to close the session when done with the API.
        """
        await self.session.close()
