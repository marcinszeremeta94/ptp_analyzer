def get_help():
    return  f'PTP ANALYSER\n'\
            f'---------------------------------------------------------------------------------------\n'\
            f'Tool providing complex analysis of pcap files containingPTPv2 over Ethernet.\n'\
            f'Tested with tcpdump pcaps from ordinaryclock one-step mode. \n'\
            f'Should handle two-step and transparentclocks tcpdumps as well.\n\n'\
            f'Analysis provide:\n'\
            f'\t1. Checking amount of particular PTP packet type\n'\
            f'\t2. Announce data change within pcap file\n'\
            f'\t3. MAC addresses and Clock ID consistency\n'\
            f'\t4. Consistency in PTP meassage sequence ID increasing\n'\
            f'\t5. Detection and check of message rate errors\n'\
            f'\t6. Providing statistics of intervals and rates\n'\
            f'\t7. Checking PTP messages not in sequence (one-step-mode)\n'\
            f'\t8. Providing statistics of intervals between PTP message exchanges\n\n'\
            f'USAGE:\n'\
            f'PtpAnalyzer.py can be run as Python script or Bash script:\n'\
            f'\tpython PtpAnalyzer.py [FILENAME] [options]\n'\
            f'\t./PtpAnalyzer.py [FILENAME] [options]\n\n'\
            f'Application works under Linux and Windows as well.\n'\
            f'Argument [FILENAME] is mandatory. Pcap file is dispatched by scapy,\n'\
            f'which does not accept tcpdumps taken from all interfaces (Linux cooked capture).\n'\
            f'All other options are, well optional and not required. Default arguments are marked\n'\
            f'as DEFAULT in argument list below. Order of options does not matter, however\n'\
            f'if more than one option impact the same functionality last one is taken.\n'\
            f'Analysis depth arguments adds up.\n\n'\
            f'Analysis reports are stored in <Ptp Analyser Path>/reports/ \n'\
            f'as .log files named same as provided pcap file\n\n'\
            f'ARGUMENTS:\n'\
            f'-v or --verbose\t\t\t\tMore logging and printing, all warnings and wrong frames time\n'\
            f'-l or --no-logs\t\t\t\tTurns off logging to file\n'\
            f'-p or --no-prints\t\t\tTurns off printing logs to console\n'\
            f'--full\t\t\t\t\tAnalysis Depth - all available analysis - DEFAULT\n'\
            f'--announce\t\t\t\tAnalysis Depth - announce PTP messages check\n'\
            f'--ports\t\t\t\t\tAnalysis Depth - MAC and Clock ID check\n'\
            f'--sequenceId\t\t\t\tAnalysis Depth - PTP message sequence ID check\n'\
            f'--timing\t\t\t\tAnalysis Depth - Message rate and interval check with statistics\n'\
            f'--match\t\t\t\t\tAnalysis Depth - One step mesage exchange check with statistics\n'\
            f'-h or --help\t\t\t\tPrint help\n\n'           
