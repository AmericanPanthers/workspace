LUKS CRYPT
==========

Keys are derived from yubikey+password. Yubikey provides as physical token that is physically
handed over when responsibility changes. Passwords are unique to each new yubikey holder.

**Notes:**

    - All LUKS (crypto) operations require Tails OS to be booted with an admin password
    - This system requires LUKS (Linux) and a YubiKey


Vault Script
------------

The ~/bin directory includes a "vault" script that simplifies interacting with
LUKS-encrypted volumes.

Default vault directory: "$HOME/Persistent/shared/.vault"

.. todo:: Need to explain this better (TODO)

    - You should copy/paste this "vault" structure and use it in another directory
    - Use ``vault -r "$HOME/Persistent/Vault" -o $NAME`` (or similar) to open

To Unlock::

    vault -o $NAME

To View Contents::

    ls ~/Persistent/shared/vault/mnt/$NAME/

To Lock::

    vault -c $NAME

Manual Steps
------------

To Create::

    mkdir "$CRYPT_ROOT/mnt/$NAME"
    dd if=/dev/urandom of="$CRYPT_ROOT/headers/$NAME" bs=1MB count=10
    dd if=/dev/urandom of="$CRYPT_ROOT/crypts/$NAME" bs=$SIZE count=1
    sudo cryptsetup luksFormat "$CRYPT_ROOT/crypts/$NAME" --header "$CRYPT_ROOT/headers/$NAME" -s 512 --align-payload=0
    sudo cryptsetup open "$CRYPT_ROOT/crypts/$NAME" --header "$CRYPT_ROOT/headers/$NAME $NAME"
    sudo mkfs.ext2 "/dev/mapper/$NAME"
    sudo mount "/dev/mapper/$NAME" "$CRYPT_ROOT/mnt/$NAME"
    sudo chown 1000:1000 "$CRYPT_ROOT/mnt/$NAME"

To Open::

    sudo cryptsetup open "$CRYPT_ROOT/crypts/$NAME" --header "$CRYPT_ROOT/headers/$NAME" "$NAME"
    sudo mount "/dev/mapper/$NAME" "$CRYPT_ROOT/mnt/$NAME"

To Close::

    sudo umount "$CRYPT_ROOT/mnt/$NAME"
    sudo cryptsetup close "$NAME"
