from dataclasses import dataclass
from .PTPv2 import PTPv2, PtpType, PTP_MSG_TYPE
import time


class PtpAnnounceSignal:

    def __init__(self, logger, time_offset=0):
        self.time_offset = time_offset
        self._logger = logger
        self._announce_data = AnnounceData()

    def check_announce_consistency(self, announce=[]):
        if not announce:
            self._logger.info('PTP Announce list empty.')
            return
        if not self._is_input_valid(announce):
            self._logger.error('PTP Announce input invalid!')
            return
        self._announce_data = AnnounceData(announce[0])
        self._logger.info(self.__repr__())
        self._check_stream_consistency(announce)

    def _check_stream_consistency(self, announce):
        inconsistent_counter = 0
        for msg in announce:
            if AnnounceData(msg) != self._announce_data:
                inconsistent_counter += 1
                self._logger.warning(f'Announce msg data inconsistent with first announce data')
                self._logger.msg_timing(msg, self.time_offset)
        if inconsistent_counter > 0:
            self._logger.warning(f'Number of inconsistencies: {inconsistent_counter}')
        else:
            self._logger.info(f'PTP Announce stream: [OK]')

    def _is_input_valid(self, msgs):
        for msg in msgs:
            if PtpType.get_ptp_msg_type(msg) != PTP_MSG_TYPE.ANNOUNCE_MSG:
                return False
        return True

    @property
    def announce_data(self):
        return self._announce_data

    def __repr__(self):
        return self._announce_data.__repr__()


@dataclass
class AnnounceData:
    def __init__(self, announce: PTPv2 = PTPv2()):
        if PtpType.is_announce(announce):
            self.clock_id = announce.sourcePortIdentity
            self.origin_utc_offset = announce.utcOffset
            self.priority_1 = announce.priority1
            self.grandmaster_clock_class = announce.grandmasterClockClass
            self.grandmaster_clock_accuracy = announce.grandmasterClockAccuracy
            self.grandmaster_clock_variance = announce.grandmasterClockVariance
            self.priority_2 = announce.priority2
            self.grandmaster_clock_id = announce.grandmasterClockId
            self.local_steps_removed = announce.localStepsRemoved
            self.time_source = announce.timeSource
        else:
            self.clock_id = 0
            self.origin_utc_offset = 0
            self.priority_1 = 0
            self.grandmaster_clock_class = 0
            self.grandmaster_clock_accuracy = 0xFE
            self.grandmaster_clock_variance = 0
            self.priority_2 = 0
            self.grandmaster_clock_id = 0
            self.local_steps_removed = 0
            self.time_source = 0

    def __repr__(self):
        return f'PTP signal source data from announce msg:\n\tClock ID: {self.clock_id},\n\tUTC Offset: '\
            f'{self.origin_utc_offset},\n\tpriority1: {self.priority_1},\n\tgrandmasterClockClass: '\
            f'{self.grandmaster_clock_class},\n\tgrandmasterClockAccuracy: {PTPv2.CLK_ACCURACY[self.grandmaster_clock_accuracy]},'\
            f'\n\tgrandmasterClockVariance: {self.grandmaster_clock_variance},\n\tpriority2: {self.priority_2},'\
            f'\n\tgrandmasterClockIdentity: 0x{self.grandmaster_clock_id.hex()},\n\tlocalStepsRemoved: '\
            f'{self.local_steps_removed},\n\tTimeSource: {PTPv2.TIME_SOURCE[self.time_source]}'
