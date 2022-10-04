from tkinter import *
from PIL import Image,ImageTk

def distance():

    def convert():
       #local variable for km to m converter
       kmval = kmVar.get()
       mval = metreVar.get()
       #local variable for mile to km
       kmil = kmmileVar.get()
       mile = mileVar.get()
       #local variable for metre to inch converter
       minch = minchVar.get()
       inch = inchVar.get()
       #local variable for metre to feet converter
       mfeet = mfeetVar.get()
       feet = feetVar.get()

       #converting from km to metre
       if kmVar.get() != 0.0:
         convkm = kmval * 1000
         metreVar.set(convkm)

       elif metreVar.get() != 0.0:
         convm = mval / 1000
         kmVar.set(convm)
       #converting from mile to km
       if kmmileVar.get() !=0.0 :
           convmil = kmil / 1.609
           mileVar.set(convmil)
       elif mileVar.get() != 0.0:
           convk= mile * 1.609
           kmmileVar.set(convk)

       # converting from inch to metre
       if minchVar.get() != 0.0:
            convim = minch * 39.37
            inchVar.set(convim)

       elif inchVar.get() != 0.0:
            convin = inch / 39.37
            minchVar.set(convin)
       #convert from metre to feet
       if mfeetVar.get() != 0.0:
         convf = mfeet * 3.281
         feetVar.set(convf)

       elif feetVar.get() != 0.0:
         convmf = feet / 3.281
         mfeetVar.set(convmf)

    def reset():
      kmVar.set(int(0))
      metreVar.set(int(0))
      kmmileVar.set(int(0))
      mileVar.set(int(0))
      minchVar.set(int(0))
      inchVar.set(int(0))
      mfeetVar.set(int(0))
      feetVar.set(int(0))

    top = Toplevel()
    top.title("Distance Converter")
    ###MAIN###
    kmVar = IntVar()
    kmVar.set(int(0))
    metreVar = IntVar()
    metreVar.set(int(0))
    #convert from km to mile
    kmmileVar = IntVar()
    kmmileVar.set(int(0))
    mileVar = IntVar()
    mileVar.set(int(0))
    # convert from metre to inch variable
    minchVar = IntVar()
    minchVar.set(int(0))
    inchVar = IntVar()
    inchVar.set(int(0))
    # convet from metre to feet variable
    mfeetVar = IntVar()
    mfeetVar.set(int(0))
    feetVar = IntVar()
    feetVar.set(int(0))
    titleLabel = Label(top, text="Distance Converter", font=("times", 20),bg="yellow",width=30)
    titleLabel.grid(row=0,column=0,columnspan=5)

    kmLabel = Label(top, text="Kilometer:", font=("times", 16))
    kmLabel.grid(row=1, column=0,sticky=W,pady=10)

    metreLabel = Label(top, text="Meter:", font=("times", 16))
    metreLabel.grid(row=1, column=3,sticky=W)

    kmEntry = Entry(top, width=10, bd=5, textvariable=kmVar)
    kmEntry.grid(row=1, column=1,sticky=W)

    metreEntry = Entry(top, width=10, bd=5, textvariable=metreVar)
    metreEntry.grid(row=1, column=4,pady=20,padx=10,sticky=W)

    #converting from km to mile
    kmmilLabel = Label(top, text="Kilometer:", font=("times", 16))
    kmmilLabel.grid(row=2, column=0, sticky=W, pady=10)

    mileLabel = Label(top, text="Mile: ", font=("times", 16))
    mileLabel.grid(row=2, column=3, sticky=W)

    kmmilEntry = Entry(top, width=10, bd=5, textvariable=kmmileVar)
    kmmilEntry.grid(row=2, column=1,sticky=W)

    mileEntry = Entry(top, width=10, bd=5, textvariable=mileVar)
    mileEntry.grid(row=2, column=4,sticky=W,padx=10)

    #converting from metre to inch
    minchLabel = Label(top, text="Meter:", font=("times", 16))
    minchLabel.grid(row=3, column=0, sticky=W, pady=10)

    inchLabel = Label(top, text="Inch: ", font=("times", 16))
    inchLabel.grid(row=3, column=3, sticky=W)

    minchEntry = Entry(top, width=10, bd=5, textvariable=minchVar)
    minchEntry.grid(row=3, column=1, sticky=W)

    inchEntry = Entry(top, width=10, bd=5, textvariable=inchVar)
    inchEntry.grid(row=3, column=4, sticky=W, padx=10)
    #convert from metre to feet
    mfeetLabel = Label(top, text="Meter:", font=("times", 16))
    mfeetLabel.grid(row=4, column=0, sticky=W, pady=10)

    feetLabel = Label(top, text="Feet: ", font=("times", 16))
    feetLabel.grid(row=4, column=3, sticky=W)

    mfeetEntry = Entry(top, width=10, bd=5, textvariable=mfeetVar)
    mfeetEntry.grid(row=4, column=1, sticky=W)

    feetEntry = Entry(top, width=10, bd=5, textvariable=feetVar)
    feetEntry.grid(row=4, column=4, sticky=W, padx=10)

    #create button
    convertButton = Button(top, text="Convert", font=("times", 16), width=10,bg="green",bd=5,command=convert)
    convertButton.grid(row=5, column=0,padx=20)

    resetButton = Button(top, text="Reset", font=("times", 16),width=10, bg="blue",bd=5, command=reset)
    resetButton.grid(row=5, column=4 )
# define area funtion


def area():
    def convert():
       #local variable for m to mm converter
       msqval = msqVar.get()
       mmval = mmsqVar.get()
       #local variable for m  to cm
       msqcmval = msqcmVar.get()
       cmsqval = cmsqVar.get()
       #local variable for m to hectare converter
       msqhecval = msqhecVar.get()
       hecval = hecVar.get()
       #local variable for km to m converter
       kmsqval = kmsqmVar.get()
       msqkmVal = kmsqmVar.get()
       #local variable for km to hectare
       kmsqhval = kmsqhVar.get()
       heckmval = heckmVar.get()

       #converting from km to metre
       if msqVar.get() != 0.0:
         convkm = msqval * 1000000
         mmsqVar.set(convkm)

       elif msqcmVar.get() != 0.0:
         convm = msqcmval / 1000000
         mmsqVar.set(convm)
       #converting from m to cm
       if msqcmVar.get() !=0.0 :
           convmil = msqcmval * 10000
           cmsqVar.set(convmil)
       elif cmsqVar.get() != 0.0:
           convk= cmsqval / 10000
           msqcmVar.set(convk)

       # converting from m to hectare
       if msqhecVar.get() != 0.0:
            convim = msqhecval / 10000
            hecVar.set(convim)

       elif hecVar.get() != 0.0:
            convin = hecval * 10000
            msqhecVar.set(convin)
       #convert from kilometre to metre square
       if kmsqmVar.get() != 0.0:
         convf = kmsqval * 3.281
         msqkmVar.set(convf)

       elif kmsqhVar.get() != 0.0:
         convmf = kmsqhval / 3.281
         hecVar.set(convmf)

    def reset():
        msqVar.set(int(0))
        mmsqVar.set(int(0))
        msqcmVar.set(int(0))
        cmsqVar.set(int(0))
        msqhecVar.set(int(0))
        hecVar.set(int(0))
        kmsqmVar.set(int(0))
        msqkmVar.set(int(0))
        kmsqhVar.set(int(0))
        heckmVar.set(int(0))

    top = Toplevel()
    top.title("Area Converter")
    ###MAIN###
    #convert from metre square to mm square
    msqVar = IntVar()
    msqVar.set(int(0))
    mmsqVar = IntVar()
    mmsqVar.set(int(0))
    #convert from m square to cm square
    msqcmVar = IntVar()
    msqcmVar.set(int(0))
    cmsqVar = IntVar()
    cmsqVar.set(int(0))
    # convert from metre square to hectare
    msqhecVar = IntVar()
    msqhecVar.set(int(0))
    hecVar = IntVar()
    hecVar.set(int(0))
    # convet from kilometre square to hectare
    kmsqmVar = IntVar()
    kmsqmVar.set(int(0))
    msqkmVar = IntVar()
    msqkmVar.set(int(0))
    #convert from kilomere square to hectare
    kmsqhVar = IntVar()
    kmsqhVar.set(int(0))
    heckmVar = IntVar()
    heckmVar.set(int(0))

    titleLabel = Label(top, text="Area Converter", font=("times", 20),bg="yellow",width=38)
    titleLabel.grid(row=0,column=0,columnspan=5)

    msqLabel = Label(top, text="Metre Square:", font=("times", 16))
    msqLabel.grid(row=1, column=0,sticky=W,pady=10)

    mmsqLabel = Label(top, text="Milimetre Square:", font=("times", 16))
    mmsqLabel.grid(row=1, column=3,sticky=W)

    msqEntry = Entry(top, width=10, bd=5, textvariable=msqVar)
    msqEntry.grid(row=1, column=1,sticky=W)

    mmsqEntry = Entry(top, width=10, bd=5, textvariable=mmsqVar)
    mmsqEntry.grid(row=1, column=4,pady=20,padx=10,sticky=W)

    #converting from km to mile
    msqcmLabel = Label(top, text="Metre Square:", font=("times", 16))
    msqcmLabel.grid(row=2, column=0, sticky=W, pady=10)

    cmLabel = Label(top, text="Centimetre Square: ", font=("times", 16))
    cmLabel.grid(row=2, column=3, sticky=W)

    msqcmEntry = Entry(top, width=10, bd=5, textvariable=msqcmVar)
    msqcmEntry.grid(row=2, column=1,sticky=W)

    cmEntry = Entry(top, width=10, bd=5, textvariable=cmsqVar)
    cmEntry.grid(row=2, column=4,sticky=W,padx=10)

    #converting from metre to hectare
    msqhecLabel = Label(top, text="Metre:", font=("times", 16))
    msqhecLabel.grid(row=3, column=0, sticky=W, pady=10)

    hecLabel = Label(top, text="Hectare: ", font=("times", 16))
    hecLabel.grid(row=3, column=3, sticky=W)

    msqhecEntry = Entry(top, width=10, bd=5, textvariable=msqhecVar)
    msqhecEntry.grid(row=3, column=1, sticky=W)

    hecEntry = Entry(top, width=10, bd=5, textvariable=hecVar)
    hecEntry.grid(row=3, column=4, sticky=W, padx=10)
    #convert from kilometre to metre square
    kmsqmLabel = Label(top, text="Kilometre:", font=("times", 16))
    kmsqmLabel.grid(row=4, column=0, sticky=W, pady=10)

    msqkmLabel = Label(top, text="Metre Square: ", font=("times", 16))
    msqkmLabel.grid(row=4, column=3, sticky=W)

    kmsqmEntry = Entry(top, width=10, bd=5, textvariable=kmsqmVar)
    kmsqmEntry.grid(row=4, column=1, sticky=W)

    msqkmEntry = Entry(top, width=10, bd=5, textvariable=msqkmVar)
    msqkmEntry.grid(row=4, column=4, sticky=W, padx=10)

    kmsqhLabel = Label(top, text="Kilometre Square:", font=("times", 16))
    kmsqhLabel.grid(row=5, column=0, sticky=W, pady=10)

    heckmLabel = Label(top, text="Hectare:", font=("times", 16))
    heckmLabel.grid(row=5, column=3, sticky=W)

    kmsqhEntry = Entry(top, width=10, bd=5, textvariable=kmsqhVar)
    kmsqhEntry.grid(row=5, column=1, sticky=W)

    heckmEntry = Entry(top, width=10, bd=5, textvariable=heckmVar)
    heckmEntry.grid(row=5, column=4, sticky=W, padx=10)

    #create button
    convertButton = Button(top, text="Convert", font=("times", 16), width=10,bg="green",bd=5,command=convert)
    convertButton.grid(row=6, column=0,padx=20)

    resetButton = Button(top, text="Reset", font=("times", 16),width=10, bg="blue",bd=5, command=reset)
    resetButton.grid(row=6, column=4 )
#volume converter


def volume():
    def convert():
        # local variable for m to mm converter
        mcubl = mcublVar.get()
        litre = litreVar.get()
        # local variable for m  to cm
        mil = milVar.get()
        cmcubmil = cmcubmilVar.get()
        # local variable for m to hectare converter
        mcubd = mcubdVar.get()
        dmcub = dmcubVar.get()
        # local variable for km to m converter
        mcubc = mcubcVar.get()
        cmcub = cmcubVar.get()

        # converting from msq to litre
        if mcublVar.get() != 0.0:
            convkm = mcubl * 1000
            litreVar.set(convkm)

        elif litreVar.get() != 0.0:
            convm = litre / 1000
            mcublVar.set(convm)
        # converting from ml to cm sq
        if milVar.get() != 0.0:
            convmil = int(mil)
            cmcubmilVar.set(convmil)
        elif cmcubmilVar.get() != 0.0:
            convk = cmcubmil
            milVar.set(convk)

        # converting from m sq to dm sq
        if mcubdVar.get() != 0.0:
            convim = mcubd * 1000
            dmcubVar.set(convim)

        elif dmcubVar.get() != 0.0:
            convin = dmcub / 1000
            mcubdVar.set(convin)
        # convert from m sq to cm square
        if mcubcVar.get() != 0.0:
            convf = mcubc * 10 ** 6
            cmcubVar.set(convf)

        elif cmcubVar.get() != 0.0:
            convmf = cmcub / 10 ** 6
            cmcub.set(convmf)

    def reset():
        mcublVar.set(int(0))
        litreVar.set(int(0))
        milVar.set(int(0))
        cmcubmilVar.set(int(0))
        mcubdVar.set(int(0))
        dmcubVar.set(int(0))
        mcubcVar.set(int(0))
        cmcubVar.set(int(0))

    top = Toplevel()
    top.title("Volume Converter")
    ###MAIN###
    # convert from metre square to mm square
    mcublVar = IntVar()
    mcublVar.set(int(0))
    litreVar = IntVar()
    litreVar.set(int(0))
    # convert from m square to cm square
    mcubdVar = IntVar()
    mcubdVar.set(int(0))
    dmcubVar = IntVar()
    dmcubVar.set(int(0))
    # convert from metre square to hectare
    mcubcVar = IntVar()
    mcubcVar.set(int(0))
    cmcubVar = IntVar()
    cmcubVar.set(int(0))
    # convet from kilometre square to hectare
    milVar = IntVar()
    milVar.set(int(0))
    cmcubmilVar = IntVar()
    cmcubmilVar.set(int(0))

    titleLabel = Label(top, text="Volume Converter", font=("times", 20), bg="yellow", width=38)
    titleLabel.grid(row=0, column=0, columnspan=5)

    msqLabel = Label(top, text="Metre Cube:", font=("times", 16))
    msqLabel.grid(row=1, column=0, sticky=W, pady=10)

    mmsqLabel = Label(top, text="Litre:", font=("times", 16))
    mmsqLabel.grid(row=1, column=3, sticky=W)

    msqEntry = Entry(top, width=10, bd=5, textvariable=mcublVar)
    msqEntry.grid(row=1, column=1, sticky=W)

    mmsqEntry = Entry(top, width=10, bd=5, textvariable=litreVar)
    mmsqEntry.grid(row=1, column=4, pady=20, padx=10, sticky=W)

    # converting from km to mile
    msqcmLabel = Label(top, text="Mililitre:", font=("times", 16))
    msqcmLabel.grid(row=2, column=0, sticky=W, pady=10)

    cmLabel = Label(top, text="Centimetre Cube: ", font=("times", 16))
    cmLabel.grid(row=2, column=3, sticky=W)

    msqcmEntry = Entry(top, width=10, bd=5, textvariable=milVar)
    msqcmEntry.grid(row=2, column=1, sticky=W)

    cmEntry = Entry(top, width=10, bd=5, textvariable=cmcubmilVar)
    cmEntry.grid(row=2, column=4, sticky=W, padx=10)

    # converting from metre to hectare
    msqhecLabel = Label(top, text="Metre Cube:", font=("times", 16))
    msqhecLabel.grid(row=3, column=0, sticky=W, pady=10)

    hecLabel = Label(top, text="Decimetre Cube: ", font=("times", 16))
    hecLabel.grid(row=3, column=3, sticky=W)

    msqhecEntry = Entry(top, width=10, bd=5, textvariable=mcubdVar)
    msqhecEntry.grid(row=3, column=1, sticky=W)

    hecEntry = Entry(top, width=10, bd=5, textvariable=dmcubVar)
    hecEntry.grid(row=3, column=4, sticky=W, padx=10)
    # convert from kilometre to metre square
    kmsqmLabel = Label(top, text="Metre Cube:", font=("times", 16))
    kmsqmLabel.grid(row=4, column=0, sticky=W, pady=10)

    msqkmLabel = Label(top, text="Centimetre Cube: ", font=("times", 16))
    msqkmLabel.grid(row=4, column=3, sticky=W)

    kmsqmEntry = Entry(top, width=10, bd=5, textvariable=mcubcVar)
    kmsqmEntry.grid(row=4, column=1, sticky=W)

    msqkmEntry = Entry(top, width=10, bd=5, textvariable=cmcubVar)
    msqkmEntry.grid(row=4, column=4, sticky=W, padx=10)

    # create button
    convertButton = Button(top, text="Convert", font=("times", 16), width=10, bg="green", bd=5, command=convert)
    convertButton.grid(row=5, column=0, padx=20)

    resetButton = Button(top, text="Reset", font=("times", 16), width=10, bg="blue", bd=5, command=reset)
    resetButton.grid(row=5, column=3)

# volume converter


def time():
    def convert():
       #local variable for f to min converter
       mcubl = hminVar.get()
       litre = minhVar.get()
       #local variable for h  to s
       mil = hsVar.get()
       cmcubmil = shVar.get()
       #local variable for minto s converter
       mcubd = minsVar.get()
       dmcub = sminVar.get()
       #local variable for s to ms converter
       mcubc = smsVar.get()
       cmcub = mssVar.get()


       #converting from hour to minute
       if hminVar.get() != 0.0:
         convkm = mcubl * 60
         minhVar.set(convkm)

       elif minhVar.get() != 0.0:
         convm = litre / 60
         hminVar.set(convm)
       #converting from h to s
       if hsVar.get() !=0.0 :
           convmil = mil *3600
           shVar.set(convmil)
       elif shVar.get() != 0.0:
           convk= cmcubmil / 3600
           hsVar.set(convk)

       # converting from min  to s
       if minsVar.get() != 0.0:
            convim = mcubd * 60
            sminVar.set(convim)

       elif sminVar.get() != 0.0:
            convin = dmcub / 60
            minsVar.set(convin)
       #convert from ms  to s
       if smsVar.get() != 0.0:
         convf = mcubc * 60
         mssVar.set(convf)

       elif mssVar.get() != 0.0:
         convmf = cmcub / 60
         smsVar.set(convmf)

    def reset():
        hminVar.set(int(0))
        minhVar.set(int(0))
        hsVar.set(int(0))
        shVar.set(int(0))
        minsVar.set(int(0))
        sminVar.set(int(0))
        smsVar.set(int(0))
        mssVar.set(int(0))

    top = Toplevel()
    top.title("Time Converter")
    ###MAIN###
    #convert from hour  to minute
    hminVar = IntVar()
    hminVar.set(int(0))
    minhVar = IntVar()
    minhVar.set(int(0))
    #convert from hour to second
    hsVar = IntVar()
    hsVar.set(int(0))
    shVar = IntVar()
    shVar.set(int(0))
    # convert from minute to second
    minsVar = IntVar()
    minsVar.set(int(0))
    sminVar = IntVar()
    sminVar.set(int(0))
    # convet from second to milisecond
    smsVar = IntVar()
    smsVar.set(int(0))
    mssVar = IntVar()
    mssVar.set(int(0))


    titleLabel = Label(top, text="Volume Converter", font=("times", 20),bg="yellow",width=33)
    titleLabel.grid(row=0,column=0,columnspan=5)

    msqLabel = Label(top, text="Hour:", font=("times", 16))
    msqLabel.grid(row=1, column=0,sticky=W,pady=10)

    mmsqLabel = Label(top, text="Minute:", font=("times", 16))
    mmsqLabel.grid(row=1, column=3,sticky=W)

    msqEntry = Entry(top, width=10, bd=5, textvariable=hminVar)
    msqEntry.grid(row=1, column=1,sticky=W)

    mmsqEntry = Entry(top, width=10, bd=5, textvariable=minhVar)
    mmsqEntry.grid(row=1, column=4,pady=20,padx=10,sticky=W)

    #converting from km to mile
    msqcmLabel = Label(top, text="Hour:", font=("times", 16))
    msqcmLabel.grid(row=2, column=0, sticky=W, pady=10)

    cmLabel = Label(top, text="Second: ", font=("times", 16))
    cmLabel.grid(row=2, column=3, sticky=W)

    msqcmEntry = Entry(top, width=10, bd=5, textvariable=hsVar)
    msqcmEntry.grid(row=2, column=1,sticky=W)

    cmEntry = Entry(top, width=10, bd=5, textvariable=shVar)
    cmEntry.grid(row=2, column=4,sticky=W,padx=10)

    #converting from metre to hectare
    msqhecLabel = Label(top, text="Minute:", font=("times", 16))
    msqhecLabel.grid(row=3, column=0, sticky=W, pady=10)

    hecLabel = Label(top, text="Second: ", font=("times", 16))
    hecLabel.grid(row=3, column=3, sticky=W)

    msqhecEntry = Entry(top, width=10, bd=5, textvariable=minsVar)
    msqhecEntry.grid(row=3, column=1, sticky=W)

    hecEntry = Entry(top, width=10, bd=5, textvariable=sminVar)
    hecEntry.grid(row=3, column=4, sticky=W, padx=10)
    #convert from kilometre to metre square
    kmsqmLabel = Label(top, text="Second:", font=("times", 16))
    kmsqmLabel.grid(row=4, column=0, sticky=W, pady=10)

    msqkmLabel = Label(top, text="Milisecond: ", font=("times", 16))
    msqkmLabel.grid(row=4, column=3, sticky=W)

    kmsqmEntry = Entry(top, width=10, bd=5, textvariable=smsVar)
    kmsqmEntry.grid(row=4, column=1, sticky=W)

    msqkmEntry = Entry(top, width=10, bd=5, textvariable=mssVar)
    msqkmEntry.grid(row=4, column=4, sticky=W, padx=10)


    #create button
    convertButton = Button(top, text="Convert", font=("times", 16), width=10,bg="green",bd=5,command=convert)
    convertButton.grid(row=5, column=0,padx=20)

    resetButton = Button(top, text="Reset", font=("times", 16),width=10, bg="blue",bd=5, command=reset)
    resetButton.grid(row=5, column=4 )


#speed converter

def speed():
    def convert():
       #local variable for f to min converter
       mcubl = kmhVar.get()
       litre = mshVar.get()
       #local variable for h  to s
       mil = kmhmVar.get()
       cmcubmil = mhVar.get()
       #local variable for minto s converter
       mcubd = mimVar.get()
       dmcub = msmVar.get()
       #local variable for s to ms converter
       mcubc = kmfVar.get()
       cmcub = fkmVar.get()


       #converting from hour to minute
       if kmhVar.get() != 0.0:
         convkm = mcubl / 3.6
         mshVar.set(convkm)

       elif mshVar.get() != 0.0:
         convm = litre * 3.6
         kmhVar.set(convm)
       #converting from h to s
       if kmhmVar.get() !=0.0 :
           convmil = mil / 1.609
           mhVar.set(convmil)
       elif mhVar.get() != 0.0:
           convk= cmcubmil * 1.609
           kmhmVar.set(convk)

       # converting from min  to s
       if mimVar.get() != 0.0:
            convim = mcubd / 2.237
            msmVar.set(convim)

       elif msmVar.get() != 0.0:
            convin = dmcub * 2.237
            mimVar.set(convin)
       #convert from ms  to s
       if kmfVar.get() != 0.0:
         convf = mcubc / 1.097
         fkmVar.set(convf)

       elif fkmVar.get() != 0.0:
         convmf = cmcub *  1.097

         kmfVar.set(convmf)

    def reset():
        kmhVar.set(int(0))
        mshVar.set(int(0))
        kmhmVar.set(int(0))
        mhVar.set(int(0))
        mimVar.set(int(0))
        msmVar.set(int(0))
        kmfVar.set(int(0))
        fkmVar.set(int(0))

    top = Toplevel()
    top.title("Speed Converter")
    ###MAIN###
    #convert from hour  to minute
    kmhVar = IntVar()
    kmhVar.set(int(0))
    mshVar = IntVar()
    mshVar.set(int(0))
    #convert from hour to second
    kmhmVar = IntVar()
    kmhmVar.set(int(0))
    mhVar = IntVar()
    mhVar.set(int(0))
    # convert from minute to second
    mimVar = IntVar()
    mimVar.set(int(0))
    msmVar = IntVar()
    msmVar.set(int(0))
    # convet from second to milisecond
    kmfVar = IntVar()
    kmfVar.set(int(0))
    fkmVar = IntVar()
    fkmVar.set(int(0))


    titleLabel = Label(top, text="Speed Converter", font=("times", 20),bg="yellow",width=30)
    titleLabel.grid(row=0,column=0,columnspan=5)

    msqLabel = Label(top, text="Kilometre/Hour:", font=("times", 16))
    msqLabel.grid(row=1, column=0,sticky=W,pady=10)

    mmsqLabel = Label(top, text="Metre/Second:", font=("times", 16))
    mmsqLabel.grid(row=1, column=3,sticky=W)

    msqEntry = Entry(top, width=10, bd=5, textvariable=kmhVar)
    msqEntry.grid(row=1, column=1,sticky=W)

    mmsqEntry = Entry(top, width=10, bd=5, textvariable=mshVar)
    mmsqEntry.grid(row=1, column=4,pady=20,padx=10,sticky=W)

    #converting from km to mile
    msqcmLabel = Label(top, text="Kilometre/Hour:", font=("times", 16))
    msqcmLabel.grid(row=2, column=0, sticky=W, pady=10)

    cmLabel = Label(top, text="Mile/Hour: ", font=("times", 16))
    cmLabel.grid(row=2, column=3, sticky=W)

    msqcmEntry = Entry(top, width=10, bd=5, textvariable=kmhmVar)
    msqcmEntry.grid(row=2, column=1,sticky=W)

    cmEntry = Entry(top, width=10, bd=5, textvariable=mhVar)
    cmEntry.grid(row=2, column=4,sticky=W,padx=10)

    #converting from metre to hectare
    msqhecLabel = Label(top, text="Mile/Hour:", font=("times", 16))
    msqhecLabel.grid(row=3, column=0, sticky=W, pady=10)

    hecLabel = Label(top, text="Metre/Second: ", font=("times", 16))
    hecLabel.grid(row=3, column=3, sticky=W)

    msqhecEntry = Entry(top, width=10, bd=5, textvariable=mshVar)
    msqhecEntry.grid(row=3, column=1, sticky=W)

    hecEntry = Entry(top, width=10, bd=5, textvariable=mimVar)
    hecEntry.grid(row=3, column=4, sticky=W, padx=10)
    #convert from kilometre to metre square
    kmsqmLabel = Label(top, text="Kilometre/Hour:", font=("times", 16))
    kmsqmLabel.grid(row=4, column=0, sticky=W, pady=10)

    msqkmLabel = Label(top, text="Feet/Second: ", font=("times", 16))
    msqkmLabel.grid(row=4, column=3, sticky=W)

    kmsqmEntry = Entry(top, width=10, bd=5, textvariable=kmfVar)
    kmsqmEntry.grid(row=4, column=1, sticky=W)

    msqkmEntry = Entry(top, width=10, bd=5, textvariable=fkmVar)
    msqkmEntry.grid(row=4, column=4, sticky=W, padx=10)


    #create button
    convertButton = Button(top, text="Convert", font=("times", 16), width=10,bg="green",bd=5,command=convert)
    convertButton.grid(row=5, column=0,padx=20)

    resetButton = Button(top, text="Reset", font=("times", 16),width=10, bg="blue",bd=5, command=reset)
    resetButton.grid(row=5, column=4 )

#Temperature converter

def temperature():
    def convert():
        # local variable for f to min converter
        mcubl = celkVar.get()
        litre = kcelVar.get()
        # local variable for h  to s
        mil = celfVar.get()
        cmcubmil = fcelVar.get()
        # local variable for minto s converter
        mcubd = kelfVar.get()
        dmcub = fkelVar.get()

        # converting from hour to minute
        if celkVar.get() != 0.0:
            convkm = mcubl + 273
            kcelVar.set(convkm)

        elif kcelVar.get() != 0.0:
            convm = litre - 273
            celkVar.set(convm)
        # converting from h to s
        if celfVar.get() != 0.0:
            convmil = (mil * 9/5)+32
            fcelVar.set(convmil)
        elif fcelVar.get() != 0.0:
            convk = (cmcubmil - 32)* 5/9
            celfVar.set(convk)

        # converting from min  to s
        if kelfVar.get() != 0.0:
            convim = (mcubd - 273) *9/5+32
            fkelVar.set(convim)

        elif kelfVar.get() != 0.0:
            convin = (dmcub - 32) *5/9+273
            fkelVar.set(convin)

    def reset():
        celkVar.set(int(0))
        kcelVar.set(int(0))
        celfVar.set(int(0))
        fcelVar.set(int(0))
        kelfVar.set(int(0))
        fkelVar.set(int(0))

    top = Toplevel()
    top.title("Temperature Converter")
    ###MAIN###
    # convert from hour  to minute
    celkVar = IntVar()
    celkVar.set(int(0))
    kcelVar = IntVar()
    kcelVar.set(int(0))
    # convert from hour to second
    celfVar = IntVar()
    celfVar.set(int(0))
    fcelVar = IntVar()
    fcelVar.set(int(0))
    # convert from minute to second
    kelfVar = IntVar()
    kelfVar.set(int(0))
    fkelVar = IntVar()
    fkelVar.set(int(0))

    titleLabel = Label(top, text="Temperature Converter", font=("times", 20), bg="yellow", width=33)
    titleLabel.grid(row=0, column=0, columnspan=5)

    msqLabel = Label(top, text="Celsius:", font=("times", 16))
    msqLabel.grid(row=1, column=0, sticky=W, pady=10)

    mmsqLabel = Label(top, text="Kelvin:", font=("times", 16))
    mmsqLabel.grid(row=1, column=3, sticky=W)

    msqEntry = Entry(top, width=10, bd=5, textvariable=celkVar)
    msqEntry.grid(row=1, column=1, sticky=W)

    mmsqEntry = Entry(top, width=10, bd=5, textvariable=kcelVar)
    mmsqEntry.grid(row=1, column=4, pady=20, padx=10, sticky=W)

    # converting from km to mile
    msqcmLabel = Label(top, text="Celsius:", font=("times", 16))
    msqcmLabel.grid(row=2, column=0, sticky=W, pady=10)

    cmLabel = Label(top, text="Fahrenheit:", font=("times", 16))
    cmLabel.grid(row=2, column=3, sticky=W)

    msqcmEntry = Entry(top, width=10, bd=5, textvariable=celfVar)
    msqcmEntry.grid(row=2, column=1, sticky=W)

    cmEntry = Entry(top, width=10, bd=5, textvariable=fcelVar)
    cmEntry.grid(row=2, column=4, sticky=W, padx=10)

    # converting from metre to hectare
    msqhecLabel = Label(top, text="Kelvin:", font=("times", 16))
    msqhecLabel.grid(row=3, column=0, sticky=W, pady=10)

    hecLabel = Label(top, text="Fahrenheit: ", font=("times", 16))
    hecLabel.grid(row=3, column=3, sticky=W)

    msqhecEntry = Entry(top, width=10, bd=5, textvariable=kelfVar)
    msqhecEntry.grid(row=3, column=1, sticky=W)

    hecEntry = Entry(top, width=10, bd=5, textvariable=fkelVar)
    hecEntry.grid(row=3, column=4, sticky=W, padx=10)

    # create button
    convertButton = Button(top, text="Convert", font=("times", 16), width=10, bg="green", bd=5, command=convert)
    convertButton.grid(row=5, column=0, padx=20)

    resetButton = Button(top, text="Reset", font=("times", 16), width=10, bg="blue", bd=5, command=reset)
    resetButton.grid(row=5, column=4)

def weight():
    def convert():
       #local variable for f to min converter
       mcubl = kggVar.get()
       litre = gkgVar.get()
       #local variable for h  to s
       mil = kgtoneVar.get()
       cmcubmil = tonekgVar.get()
       #local variable for minto s converter
       mcubd = kgqinVar.get()
       dmcub = qinkgVar.get()
       #local variable for s to ms converter
       mcubc = kgpoundVar.get()
       cmcub = poundkgVar.get()


       #converting from hour to minute
       if kggVar.get() != 0.0:
         convkm = mcubl * 1000
         gkgVar.set(convkm)

       elif gkgVar.get() != 0.0:
         convm = litre / 1000
         kggVar.set(convm)
       #converting from h to s
       if kgtoneVar.get() !=0.0 :
           convmil = mil / 1000
           tonekgVar.set(convmil)
       elif tonekgVar.get() != 0.0:
           convk= cmcubmil * 1000
           kgtoneVar.set(convk)

       # converting from min  to s
       if kgqinVar.get() != 0.0:
            convim = mcubd / 100
            qinkgVar.set(convim)

       elif qinkgVar.get() != 0.0:
            convin = dmcub * 100
            kgqinVar.set(convin)
       #convert from ms  to s
       if kgpoundVar.get() != 0.0:
         convf = mcubc * 2.205
         poundkgVar.set(convf)

       elif poundkgVar.get() != 0.0:
         convmf = cmcub / 2.205
         kgpoundVar.set(convmf)

    def reset():
        kggVar.set(int(0))
        gkgVar.set(int(0))
        kgtoneVar.set(int(0))
        tonekgVar.set(int(0))
        kgqinVar.set(int(0))
        qinkgVar.set(int(0))
        kgpoundVar.set(int(0))
        poundkgVar.set(int(0))

    top = Toplevel()
    top.title("Weight Converter")
    ###MAIN###
    #convert from hour  to minute
    kggVar = IntVar()
    kggVar.set(int(0))
    gkgVar = IntVar()
    gkgVar.set(int(0))
    #convert from hour to second
    kgtoneVar = IntVar()
    kgtoneVar.set(int(0))
    tonekgVar = IntVar()
    tonekgVar.set(int(0))
    # convert from minute to second
    kgqinVar = IntVar()
    kgqinVar.set(int(0))
    qinkgVar = IntVar()
    qinkgVar.set(int(0))
    # convet from second to milisecond
    kgpoundVar = IntVar()
    kgpoundVar.set(int(0))
    poundkgVar = IntVar()
    poundkgVar.set(int(0))


    titleLabel = Label(top, text="Weight Converter", font=("times", 20),bg="yellow",width=32)
    titleLabel.grid(row=0,column=0,columnspan=5)

    msqLabel = Label(top, text="Kilogramme:", font=("times", 16))
    msqLabel.grid(row=1, column=0,sticky=W,pady=10)

    mmsqLabel = Label(top, text="Gramme:", font=("times", 16))
    mmsqLabel.grid(row=1, column=3,sticky=W)

    msqEntry = Entry(top, width=10, bd=5, textvariable=kggVar)
    msqEntry.grid(row=1, column=1,sticky=W)

    mmsqEntry = Entry(top, width=10, bd=5, textvariable=gkgVar)
    mmsqEntry.grid(row=1, column=4,pady=20,padx=10,sticky=W)

    #converting from km to mile
    msqcmLabel = Label(top, text="Kilogramme:", font=("times", 16))
    msqcmLabel.grid(row=2, column=0, sticky=W, pady=10)

    cmLabel = Label(top, text="Tone: ", font=("times", 16))
    cmLabel.grid(row=2, column=3, sticky=W)

    msqcmEntry = Entry(top, width=10, bd=5, textvariable=kgtoneVar)
    msqcmEntry.grid(row=2, column=1,sticky=W)

    cmEntry = Entry(top, width=10, bd=5, textvariable=tonekgVar)
    cmEntry.grid(row=2, column=4,sticky=W,padx=10)

    #converting from metre to hectare
    msqhecLabel = Label(top, text="Kilogramme:", font=("times", 16))
    msqhecLabel.grid(row=3, column=0, sticky=W, pady=10)

    hecLabel = Label(top, text="Quintal: ", font=("times", 16))
    hecLabel.grid(row=3, column=3, sticky=W)

    msqhecEntry = Entry(top, width=10, bd=5, textvariable=kgqinVar)
    msqhecEntry.grid(row=3, column=1, sticky=W)

    hecEntry = Entry(top, width=10, bd=5, textvariable=qinkgVar)
    hecEntry.grid(row=3, column=4, sticky=W, padx=10)
    #convert from kilometre to metre square
    kmsqmLabel = Label(top, text="Kilogramme:", font=("times", 16))
    kmsqmLabel.grid(row=4, column=0, sticky=W, pady=10)

    msqkmLabel = Label(top, text="Pound: ", font=("times", 16))
    msqkmLabel.grid(row=4, column=3, sticky=W)

    kmsqmEntry = Entry(top, width=10, bd=5, textvariable=kgpoundVar)
    kmsqmEntry.grid(row=4, column=1, sticky=W)

    msqkmEntry = Entry(top, width=10, bd=5, textvariable=poundkgVar)
    msqkmEntry.grid(row=4, column=4, sticky=W, padx=10)


    #create button
    convertButton = Button(top, text="Convert", font=("times", 16), width=10,bg="green",bd=5,command=convert)
    convertButton.grid(row=5, column=0,padx=20)

    resetButton = Button(top, text="Reset", font=("times", 16),width=10, bg="cyan",bd=5, command=reset)
    resetButton.grid(row=5, column=4 )


#define power function

def power():
    def convert():
       #local variable for f to min converter
       mcubl = wattjsVar.get()
       litre = jswattVar.get()
       #local variable for h  to s
       mil = wattjmVar.get()
       cmcubmil = jmwattVar.get()
       #local variable for minto s converter
       mcubd = watthVar.get()
       dmcub = hwattVar.get()



       #converting from hour to minute
       if wattjsVar.get() != 0.0:
         convkm = mcubl * 1
         jswattVar.set(convkm)

       elif jswattVar.get() != 0.0:
         convm = litre / 1
         wattjsVar.set(convm)
       #converting from h to s
       if wattjmVar.get() !=0.0 :
           convmil = mil * 60
           jmwattVar.set(convmil)
       elif jmwattVar.get() != 0.0:
           convk= cmcubmil / 60
           wattjmVar.set(convk)

       # converting from min  to s
       if watthVar.get() != 0.0:
            convim = mcubd * 3600
            hwattVar.set(convim)

       elif hwattVar.get() != 0.0:
            convin = dmcub / 3600
            watthVar.set(convin)

    def reset():
        watthVar.set(int(0))
        wattjmVar.set(int(0))
        wattjsVar.set(int(0))
        jmwattVar.set(int(0))
        jswattVar.set(int(0))
        hwattVar.set(int(0))


    top = Toplevel()
    top.title("Power Converter")
    ###MAIN###
    #convert from hour  to minute
    wattjsVar = IntVar()
    wattjsVar.set(int(0))
    jswattVar = IntVar()
    jswattVar.set(int(0))
    #convert from hour to second
    wattjmVar = IntVar()
    wattjmVar.set(int(0))
    jmwattVar = IntVar()
    jmwattVar.set(int(0))
    # convert from minute to second
    watthVar = IntVar()
    watthVar.set(int(0))
    hwattVar = IntVar()
    hwattVar.set(int(0))



    titleLabel = Label(top, text="Power Converter", font=("times", 20),bg="yellow",width=35)
    titleLabel.grid(row=0,column=0,columnspan=5)

    msqLabel = Label(top, text="Watt:", font=("times", 16))
    msqLabel.grid(row=1, column=0,sticky=W,pady=10)

    mmsqLabel = Label(top, text="Joules/second:", font=("times", 16))
    mmsqLabel.grid(row=1, column=3,sticky=W)

    msqEntry = Entry(top, width=10, bd=5, textvariable=wattjsVar)
    msqEntry.grid(row=1, column=1,sticky=W)

    mmsqEntry = Entry(top, width=10, bd=5, textvariable=jswattVar)
    mmsqEntry.grid(row=1, column=4,pady=20,padx=10,sticky=W)

    #converting from km to mile
    msqcmLabel = Label(top, text="Watt:", font=("times", 16))
    msqcmLabel.grid(row=2, column=0, sticky=W, pady=10)

    cmLabel = Label(top, text="Joules/minute:", font=("times", 16))
    cmLabel.grid(row=2, column=3, sticky=W)

    msqcmEntry = Entry(top, width=10, bd=5, textvariable=wattjmVar)
    msqcmEntry.grid(row=2, column=1,sticky=W)

    cmEntry = Entry(top, width=10, bd=5, textvariable=jmwattVar)
    cmEntry.grid(row=2, column=4,sticky=W,padx=10)

    #converting from metre to hectare
    msqhecLabel = Label(top, text="Watt:", font=("times", 16))
    msqhecLabel.grid(row=3, column=0, sticky=W, pady=10)

    hecLabel = Label(top, text="Joules/hour: ", font=("times", 16))
    hecLabel.grid(row=3, column=3, sticky=W)

    msqhecEntry = Entry(top, width=10, bd=5, textvariable=watthVar)
    msqhecEntry.grid(row=3, column=1, sticky=W)

    hecEntry = Entry(top, width=10, bd=5, textvariable=hwattVar)
    hecEntry.grid(row=3, column=4, sticky=W, padx=10)



    #create button
    convertButton = Button(top, text="Convert", font=("times", 16), width=10,bg="green",bd=5,command=convert)
    convertButton.grid(row=5, column=0,padx=20)

    resetButton = Button(top, text="Reset", font=("times", 16),width=10, bg="blue",bd=5, command=reset)
    resetButton.grid(row=5, column=4 )


#define energy function

def energy():
    def convert():
       #local variable for f to min converter
       mcubl = joulecVar.get()
       litre = cjouleVar.get()
       #local variable for h  to s
       mil = joulekiloVar.get()
       cmcubmil = kilojouleVar.get()




       #converting from hour to minute
       if joulecVar.get() != 0.0:
         convkm = mcubl / 4.184
         cjouleVar.set(convkm)

       elif cjouleVar.get() != 0.0:
         convm = litre * 4.184
         joulecVar.set(convm)
       #converting from h to s
       if joulekiloVar.get() !=0.0 :
           convmil = mil / 3600000
           kilojouleVar.set(convmil)
       elif kilojouleVar.get() != 0.0:
           convk= cmcubmil * 3600000
           joulekiloVar.set(convk)



    def reset():
        joulekiloVar.set(int(0))
        kilojouleVar.set(int(0))
        joulecVar.set(int(0))
        cjouleVar.set(int(0))



    top = Toplevel()
    top.title("Energy Converter")
    ###MAIN###
    #convert from hour  to minute
    joulecVar = IntVar()
    joulecVar.set(int(0))
    cjouleVar = IntVar()
    cjouleVar.set(int(0))
    #convert from hour to second
    joulekiloVar = IntVar()
    joulekiloVar.set(int(0))
    kilojouleVar = IntVar()
    kilojouleVar.set(int(0))



    titleLabel = Label(top, text="Energy Converter", font=("times", 20),bg="yellow",width=30)
    titleLabel.grid(row=0,column=0,columnspan=5)

    msqLabel = Label(top, text="Joule:", font=("times", 16))
    msqLabel.grid(row=1, column=0,sticky=W,pady=10)

    mmsqLabel = Label(top, text="Calories:", font=("times", 16))
    mmsqLabel.grid(row=1, column=3,sticky=W)

    msqEntry = Entry(top, width=10, bd=5, textvariable=joulecVar)
    msqEntry.grid(row=1, column=1,sticky=W)

    mmsqEntry = Entry(top, width=10, bd=5, textvariable=cjouleVar)
    mmsqEntry.grid(row=1, column=4,pady=20,padx=10,sticky=W)

    #converting from km to mile
    msqcmLabel = Label(top, text="Joule:", font=("times", 16))
    msqcmLabel.grid(row=2, column=0, sticky=W, pady=10)

    cmLabel = Label(top, text="Kilowatt/hour:", font=("times", 16))
    cmLabel.grid(row=2, column=3, sticky=W)

    msqcmEntry = Entry(top, width=10, bd=5, textvariable=joulekiloVar)
    msqcmEntry.grid(row=2, column=1,sticky=W)

    cmEntry = Entry(top, width=10, bd=5, textvariable=kilojouleVar)
    cmEntry.grid(row=2, column=4,sticky=W,padx=10)




    #create button
    convertButton = Button(top, text="Convert", font=("times", 16), width=10,bg="green",bd=5,command=convert)
    convertButton.grid(row=5, column=0,padx=20)

    resetButton = Button(top, text="Reset", font=("times", 16),width=10, bg="blue",bd=5, command=reset)
    resetButton.grid(row=5, column=4 )
fen=Tk()
fen.title("Unit Converter")
#TemperatureConverter()

title_label=Label(fen,text="Unit Converter",font=("times",20),bg="yellow",width=36)
title_label.grid(row=0,column=0,columnspan=3)
#create button
distance_button=Button(fen,text="Distance",font=("times",16),width=14,height=2,command=distance)
distance_button.grid(row=1,column=0)
area_button=Button(fen,text="Area",font=("times",16),width=14,height=2,command=area)
area_button.grid(row=1,column=1,padx=5,pady=5)
volume_button=Button(fen,text="Volume",font=("times",16),width=14,height=2,command=volume)
volume_button.grid(row=1,column=2)

time_button=Button(fen,text="Time",font=("times",16),width=14,height=2,command=time)
time_button.grid(row=2,column=0)
speed_button=Button(fen,text="Speed",font=("times",16),width=14,height=2,command=speed)
speed_button.grid(row=2,column=1,pady=5)
weight_button=Button(fen,text="Weight",font=("times",16),width=14,height=2,command=weight)
weight_button.grid(row=2,column=2)


#my=ImageTk.PhotoImage(Image.open('icontemp.png'))

temperature_button=Button(fen,text="Temperature",font=("times",16),width=14,height=2,command=temperature)
temperature_button.grid(row=3,column=0)
power_button=Button(fen,text="Power",font=("times",16),width=14,height=2,command=power)
power_button.grid(row=3,column=1)
energy_button=Button(fen,text="Energy",font=("times",16),width=14,height=2,command=energy)
energy_button.grid(row=3,column=2,pady=5)

fen.mainloop()