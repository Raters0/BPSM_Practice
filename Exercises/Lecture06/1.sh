#!/usr/bin/bash
grep -v '#' $(pwd)/blastoutput2.out | cut -f 2 > 1.result
