from typing import Optional

from pydantic import BaseModel


class ServerStats(BaseModel):
    cpu_cores: Optional[int] = 1
    cpu_current_usage: Optional[float] = None
    cpu_average_usage: Optional[float] = None
    memory_total: Optional[float] = None
    memory_percent_usage: Optional[float] = None
    disc_total: Optional[int] = None
    disc_percent_usage: Optional[float] = None
    network_download_speed: Optional[int] = None
    network_upload_speed: Optional[int] = None
    boot_time: Optional[float] = None
