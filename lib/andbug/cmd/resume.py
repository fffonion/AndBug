## Copyright 2011, Scott W. Dunlop <swdunlop@gmail.com> All rights reserved.
##
## AndBug is free software: you can redistribute it and/or modify it under 
## the terms of version 3 of the GNU Lesser General Public License as 
## published by the Free Software Foundation.
##
## AndBug is distributed in the hope that it will be useful, but WITHOUT ANY
## WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS 
## FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for 
## more details.
##
## You should have received a copy of the GNU Lesser General Public License
## along with AndBug.  If not, see <http://www.gnu.org/licenses/>.

'implementation of the "resume" command'

import andbug.command, andbug.screed

@andbug.command.action('[<name>]', shell=True)
def resume(ctxt, name=None):
    'resumes threads in the process'
    ctxt.sess.resume()

    with andbug.screed.section('Resuming Threads'):
        try:
            for t in ctxt.sess.threads(name):
                t.resume()
                andbug.screed.item('resumed %s' % t)
        finally:
            ctxt.sess.resume()